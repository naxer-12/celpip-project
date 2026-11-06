// compile_b1_pdf.js
const task = await taskSpace("render B1 pdf");
const page = task.page("p1");
const htmlPath = "file:///Users/jainamshah/Downloads/Learning%20French/French_Learning_Roadmap_Checklist_French_B1.html";
console.log("Loading B1 HTML...");
await page.goto(htmlPath, { timeout: 30000 });
console.log("Waiting for fonts...");
await page.evaluate(() => document.fonts.ready);
console.log("Printing to PDF...");
const pdfData = await page.cdp("Page.printToPDF", {
  printBackground: true,
  preferCSSPageSize: true,
  marginTop: 0,
  marginBottom: 0,
  marginLeft: 0,
  marginRight: 0
});
const fs = await import("node:fs/promises");
const outPath = "/Users/jainamshah/Downloads/Learning French/French_Learning_Roadmap_Checklist_French_B1.pdf";
await fs.writeFile(outPath, Buffer.from(pdfData.data, "base64"));
console.log("PDF created successfully at:", outPath);
await task.finish({ keep: [] });
