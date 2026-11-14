(globalThis.TURBOPACK||(globalThis.TURBOPACK=[])).push(["object"==typeof document?document.currentScript:void 0,23750,e=>{"use strict";var t=e.i(843476),n=e.i(271645),r=e.i(647163);let i=n.forwardRef(({className:e,type:n,...i},a)=>(0,t.jsx)("input",{type:n,className:(0,r.cn)("flex h-10 w-full font-medium rounded-lg border border-inpu border-slate-300 bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50",e),ref:a,...i}));i.displayName="Input",e.s(["Input",0,i])},563654,820364,998279,e=>{"use strict";let t=e=>/Failed to load chunk /i.test(e)||/module factory is not available/i.test(e)||/Loading chunk [\w]+ failed/i.test(e)||/ChunkLoadError/i.test(e)||/Cannot read properties of undefined \(reading 'call'\)/i.test(e)||/undefined is not an object \(evaluating '[^']*\.call'\)/i.test(e);e.s(["isStaleChunkMessage",0,t,"isStaleReactBundleError",0,e=>/Minified React error #3(00|10)\b/i.test(e),"reloadOnceForStaleChunk",0,()=>{let e="chunk-reload-attempt",t=Date.now(),n=0;try{n=Number(window.sessionStorage.getItem(e))||0}catch{}if(t-n<6e4)return!1;try{window.sessionStorage.setItem(e,String(t))}catch{}return window.location.reload(),!0}],820364);let n="__domInterference";`
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
`.trim();let r=e=>/network error/i.test(e)||/^failed to fetch$/i.test(e.trim())||/failed to fetch dynamically imported module/i.test(e)||/networkerror when attempting to fetch/i.test(e)||/the network connection was lost/i.test(e)||/the internet connection appears to be offline/i.test(e)||/err_internet_disconnected/i.test(e)||/^load failed$/i.test(e.trim());e.s(["isNetworkError",0,r],998279),e.s(["reportClientError",0,function(e){let i=e?.message??"",a=/not a child of this node/i.test(i)||/The node to be removed is not a child/i.test(i)||/Failed to execute '(removeChild|insertBefore|appendChild)' on 'Node'/i.test(i);if(!(!a&&(t(i)||/Connection closed/i.test(i)||r(i))))try{fetch("/api/client-error",{method:"POST",headers:{"Content-Type":"application/json"},keepalive:!0,body:JSON.stringify({message:e?.message||void 0,digest:e?.digest,url:window.location.href,release:"0be4069ad7b6748dcec03d7722c77a02cc9644b1",stack:function(e){if(!e)return;let t=e.split("\n").map(e=>e.trim()).filter(Boolean);if(0===t.length)return;let n=t[0],r=!n.includes("@")&&!n.startsWith("at ");return t.slice(+!!r,r?4:3).join(" | ").slice(0,400)||void 0}(e?.stack),isNative:!!window.appData?.isNative,domInterference:a?function(){try{let e=window[n];if(!e||"object"!=typeof e||!e.seen)return"unknown";try{e.scan?.()}catch{}let t=Object.keys(e.seen);return t.length>0?t.join(", "):"none"}catch{return}}():void 0})}).catch(()=>{})}catch{}}],563654)},772328,e=>{"use strict";e.i(247167);var t=e.i(571164),n=e.i(138544),r=e.i(271645);e.s(["useReducedMotion",0,function(){t.hasReducedMotionListener.current||(0,n.initPrefersReducedMotion)();let[e]=(0,r.useState)(t.prefersReducedMotion.current);return e}])},399847,e=>{"use strict";let t=(0,e.i(456420).default)("circle-alert",[["circle",{cx:"12",cy:"12",r:"10",key:"1mglay"}],["line",{x1:"12",x2:"12",y1:"8",y2:"12",key:"1pkeuh"}],["line",{x1:"12",x2:"12.01",y1:"16",y2:"16",key:"4dfq90"}]]);e.s(["AlertCircle",0,t],399847)},96315,e=>{"use strict";let t=(0,e.i(456420).default)("mail",[["path",{d:"m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7",key:"132q7q"}],["rect",{x:"2",y:"4",width:"20",height:"16",rx:"2",key:"izxlao"}]]);e.s(["Mail",0,t],96315)}]);