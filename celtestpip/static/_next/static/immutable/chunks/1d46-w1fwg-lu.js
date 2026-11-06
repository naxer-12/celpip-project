(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,253348,e=>{"use strict";var t=e.i(843476),n=e.i(271645),r=e.i(820364),i=e.i(563654);e.s(["default",0,function({error:e}){return(0,n.useEffect)(()=>{let t=e?.message??"",n=(0,r.isStaleChunkMessage)(t),o=(0,r.isStaleReactBundleError)(t);(0,i.reportClientError)(e),(n||o)&&(0,r.reloadOnceForStaleChunk)()},[e]),(0,t.jsx)("html",{lang:"en",children:(0,t.jsx)("body",{style:{margin:0},children:(0,t.jsx)("div",{style:{display:"flex",flexDirection:"column",alignItems:"center",justifyContent:"center",minHeight:"100vh",width:"100%",padding:"1rem",boxSizing:"border-box",background:"linear-gradient(to bottom, #dbeafe, #f3e8ff, rgba(252,231,243,0.1))",fontFamily:"ui-sans-serif, system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"},children:(0,t.jsxs)("div",{style:{display:"flex",flexDirection:"column",alignItems:"center",maxWidth:"36rem",textAlign:"center"},children:[(0,t.jsx)("img",{src:"/error.png",alt:"Error",width:200,height:300,style:{marginBottom:"2rem",height:"auto"}}),(0,t.jsx)("h1",{style:{margin:"0 0 1rem",fontSize:"2.25rem",fontWeight:900,letterSpacing:"0.025em",color:"#111827"},children:"Oops! Something went wrong"}),(0,t.jsx)("p",{style:{margin:"0 0 2rem",fontWeight:500,color:"#475569",lineHeight:1.5},children:"We apologize for the inconvenience. Our team is aware of the issue and actively working on a fix. Please try again in a few minutes."}),(0,t.jsxs)("div",{style:{display:"flex",gap:"1rem",flexWrap:"wrap",justifyContent:"center"},children:[(0,t.jsxs)("button",{type:"button",onClick:()=>{window.location.reload()},style:{display:"inline-flex",alignItems:"center",gap:"0.5rem",padding:"0.625rem 1.25rem",fontSize:"0.875rem",fontWeight:600,color:"#ffffff",background:"#2563EB",border:"none",borderRadius:"0.75rem",cursor:"pointer"},children:[(0,t.jsxs)("svg",{xmlns:"http://www.w3.org/2000/svg",width:"16",height:"16",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round","aria-hidden":"true",children:[(0,t.jsx)("path",{d:"M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"}),(0,t.jsx)("path",{d:"M3 3v5h5"}),(0,t.jsx)("path",{d:"M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"}),(0,t.jsx)("path",{d:"M16 16h5v5"})]}),"Refresh"]}),(0,t.jsxs)("button",{type:"button",onClick:()=>{window.location.href="/teacher"},style:{display:"inline-flex",alignItems:"center",gap:"0.5rem",padding:"0.625rem 1.25rem",fontSize:"0.875rem",fontWeight:600,color:"#111827",background:"#ffffff",border:"1px solid #e4e4e7",borderRadius:"0.75rem",cursor:"pointer"},children:[(0,t.jsx)("svg",{xmlns:"http://www.w3.org/2000/svg",width:"16",height:"16",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round","aria-hidden":"true",children:(0,t.jsx)("path",{d:"M7.9 20A9 9 0 1 0 4 16.1L2 22Z"})}),"Chat Support"]})]})]})})})})}])},563654,820364,998279,e=>{"use strict";let t=e=>/Failed to load chunk /i.test(e)||/module factory is not available/i.test(e)||/Loading chunk [\w]+ failed/i.test(e)||/ChunkLoadError/i.test(e)||/Cannot read properties of undefined \(reading 'call'\)/i.test(e)||/undefined is not an object \(evaluating '[^']*\.call'\)/i.test(e);e.s(["isStaleChunkMessage",0,t,"isStaleReactBundleError",0,e=>/Minified React error #3(00|10)\b/i.test(e),"reloadOnceForStaleChunk",0,()=>{let e="chunk-reload-attempt",t=Date.now(),n=0;try{n=Number(window.sessionStorage.getItem(e))||0}catch{}if(t-n<6e4)return!1;try{window.sessionStorage.setItem(e,String(t))}catch{}return window.location.reload(),!0}],820364);let n="__domInterference";`
(function () {
  try {
    var seen = {};
    var html = document.documentElement;
    function scan() {
      try {
        // Google Translate, both the browser feature and the embedded widget.
        if (html.classList.contains('translated-ltr') ||
            html.classList.contains('translated-rtl') ||
            document.querySelector('.skiptranslate')) seen['google-translate'] = 1;
        // Edge / Microsoft Translator tags every element it rewrites.
        if (document.querySelector('[_msttexthash],[_msthash],[_mstmutation]')) seen['ms-translate'] = 1;
        // Either translator's output, and the thing that actually breaks React:
        // <font> appears nowhere in our markup, so any of it came from outside.
        if (document.querySelector('font')) seen['font-tags'] = 1;
        // layout.tsx already carries suppressHydrationWarning for these, so we
        // know Grammarly is in the wild on this site.
        if (document.body && (document.body.hasAttribute('data-gr-ext-installed') ||
            document.body.hasAttribute('data-new-gr-c-s-check-loaded'))) seen['grammarly'] = 1;
        // The layout hard-codes lang="en". Anything else was set by a tool.
        var lang = html.getAttribute('lang');
        if (lang && lang !== 'en') seen['lang=' + lang.slice(0, 12)] = 1;
      } catch (e) {}
    }
    // scan is exposed so the report can take one more look on its way out. The
    // latch covers the case where the evidence is already gone; a live rescan
    // covers the opposite one, a translator that started late and left no
    // <html> marker. app/(routes)/error.tsx keeps the layout, so there the
    // rescan is reading the real, still-translated page.
    // (No backticks in here: this whole script is a template literal.)
    window.${n} = { seen: seen, scan: scan };
    scan();
    document.addEventListener('DOMContentLoaded', scan);
    window.addEventListener('load', scan);
    new MutationObserver(scan).observe(html, { attributes: true, attributeFilter: ['class', 'lang'] });
  } catch (e) {}
})();
`.trim();let r=e=>/network error/i.test(e)||/^failed to fetch$/i.test(e.trim())||/failed to fetch dynamically imported module/i.test(e)||/networkerror when attempting to fetch/i.test(e)||/the network connection was lost/i.test(e)||/the internet connection appears to be offline/i.test(e)||/err_internet_disconnected/i.test(e)||/^load failed$/i.test(e.trim());e.s(["isNetworkError",0,r],998279),e.s(["reportClientError",0,function(e){let i=e?.message??"",o=/not a child of this node/i.test(i)||/The node to be removed is not a child/i.test(i)||/Failed to execute '(removeChild|insertBefore|appendChild)' on 'Node'/i.test(i);if(!(!o&&(t(i)||/Connection closed/i.test(i)||r(i))))try{fetch("/api/client-error",{method:"POST",headers:{"Content-Type":"application/json"},keepalive:!0,body:JSON.stringify({message:e?.message||void 0,digest:e?.digest,url:window.location.href,release:"0be4069ad7b6748dcec03d7722c77a02cc9644b1",stack:function(e){if(!e)return;let t=e.split("\n").map(e=>e.trim()).filter(Boolean);if(0===t.length)return;let n=t[0],r=!n.includes("@")&&!n.startsWith("at ");return t.slice(+!!r,r?4:3).join(" | ").slice(0,400)||void 0}(e?.stack),isNative:!!window.appData?.isNative,domInterference:o?function(){try{let e=window[n];if(!e||"object"!=typeof e||!e.seen)return"unknown";try{e.scan?.()}catch{}let t=Object.keys(e.seen);return t.length>0?t.join(", "):"none"}catch{return}}():void 0})}).catch(()=>{})}catch{}}],563654)}]);