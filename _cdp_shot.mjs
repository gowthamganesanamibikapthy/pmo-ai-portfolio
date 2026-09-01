import fs from "fs";
import http from "http";

function getJson(url) {
  return new Promise((resolve, reject) => {
    http
      .get(url, (res) => {
        let data = "";
        res.on("data", (c) => (data += c));
        res.on("end", () => resolve(JSON.parse(data)));
      })
      .on("error", reject);
  });
}

const tabs = await getJson("http://127.0.0.1:9222/json");
const page = tabs.find((t) => t.type === "page" && String(t.url).includes("8501"));
if (!page) {
  console.error("no page");
  process.exit(1);
}

const ws = new WebSocket(page.webSocketDebuggerUrl);
let id = 0;
const pending = new Map();
function send(method, params = {}) {
  const msgId = ++id;
  return new Promise((resolve, reject) => {
    const t = setTimeout(() => reject(new Error("timeout " + method)), 8000);
    pending.set(msgId, {
      resolve: (v) => {
        clearTimeout(t);
        resolve(v);
      },
      reject: (e) => {
        clearTimeout(t);
        reject(e);
      },
    });
    ws.send(JSON.stringify({ id: msgId, method, params }));
  });
}
ws.onmessage = (ev) => {
  const msg = JSON.parse(ev.data);
  if (msg.id && pending.has(msg.id)) {
    const { resolve, reject } = pending.get(msg.id);
    pending.delete(msg.id);
    if (msg.error) reject(msg.error);
    else resolve(msg.result);
  }
};
await new Promise((resolve, reject) => {
  ws.onopen = resolve;
  ws.onerror = reject;
});

await send("Runtime.evaluate", {
  expression: "document.querySelector('.ai-zone-title')?.scrollIntoView({behavior:'instant', block:'start'})",
});
await new Promise((r) => setTimeout(r, 400));
const shot = await send("Page.captureScreenshot", { format: "png", fromSurface: true });
fs.writeFileSync("C:/Users/dell/Desktop/pmo-ai-portfolio/.tmp-ai.png", Buffer.from(shot.data, "base64"));
console.log("wrote ai screenshot");
ws.close();
setTimeout(() => process.exit(0), 200);
