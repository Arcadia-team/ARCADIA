"use strict";(globalThis.webpackChunk=globalThis.webpackChunk||[]).push([["vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-63debe"],{59753(a,b,c){function d(){if(!(this instanceof d))return new d;this.size=0,this.uid=0,this.selectors=[],this.selectorObjects={},this.indexes=Object.create(this.indexes),this.activeIndexes=[]}c.d(b,{f:()=>B,on:()=>A});var e,f=window.document.documentElement,g=f.matches||f.webkitMatchesSelector||f.mozMatchesSelector||f.oMatchesSelector||f.msMatchesSelector;d.prototype.matchesSelector=function(a,b){return g.call(a,b)},d.prototype.querySelectorAll=function(a,b){return b.querySelectorAll(a)},d.prototype.indexes=[];var h=/^#((?:[\w\u00c0-\uFFFF\-]|\\.)+)/g;d.prototype.indexes.push({name:"ID",selector:function(a){var b;if(b=a.match(h))return b[0].slice(1)},element:function(a){if(a.id)return[a.id]}});var i=/^\.((?:[\w\u00c0-\uFFFF\-]|\\.)+)/g;d.prototype.indexes.push({name:"CLASS",selector:function(a){var b;if(b=a.match(i))return b[0].slice(1)},element:function(a){var b=a.className;if(b){if("string"==typeof b)return b.split(/\s/);if("object"==typeof b&&"baseVal"in b)return b.baseVal.split(/\s/)}}});var j=/^((?:[\w\u00c0-\uFFFF\-]|\\.)+)/g;d.prototype.indexes.push({name:"TAG",selector:function(a){var b;if(b=a.match(j))return b[0].toUpperCase()},element:function(a){return[a.nodeName.toUpperCase()]}}),d.prototype.indexes.default={name:"UNIVERSAL",selector:function(){return!0},element:function(){return[!0]}},e="function"==typeof window.Map?window.Map:function(){function a(){this.map={}}return a.prototype.get=function(a){return this.map[a+" "]},a.prototype.set=function(a,b){this.map[a+" "]=b},a}();var k=/((?:\((?:\([^()]+\)|[^()]+)+\)|\[(?:\[[^\[\]]*\]|['"][^'"]*['"]|[^\[\]'"]+)+\]|\\.|[^ >+~,(\[\\]+)+|[>+~])(\s*,\s*)?((?:.|\r|\n)*)/g;function l(a,b){var c,d,e,f,g,h,i=(a=a.slice(0).concat(a.default)).length,j=b,l=[];do if(k.exec(""),(e=k.exec(j))&&(j=e[3],e[2]||!j)){for(c=0;c<i;c++)if(g=(h=a[c]).selector(e[1])){for(d=l.length,f=!1;d--;)if(l[d].index===h&&l[d].key===g){f=!0;break}f||l.push({index:h,key:g});break}}while(e)return l}function m(a,b){var c,d,e;for(c=0,d=a.length;c<d;c++)if(e=a[c],b.isPrototypeOf(e))return e}function n(a,b){return a.id-b.id}d.prototype.logDefaultIndexUsed=function(){},d.prototype.add=function(a,b){var c,d,f,g,h,i,j,k,n=this.activeIndexes,o=this.selectors,p=this.selectorObjects;if("string"==typeof a){for(d=0,p[(c={id:this.uid++,selector:a,data:b}).id]=c,j=l(this.indexes,a);d<j.length;d++)g=(k=j[d]).key,f=k.index,h=m(n,f),h||((h=Object.create(f)).map=new e,n.push(h)),f===this.indexes.default&&this.logDefaultIndexUsed(c),i=h.map.get(g),i||(i=[],h.map.set(g,i)),i.push(c);this.size++,o.push(a)}},d.prototype.remove=function(a,b){if("string"==typeof a){var c,d,e,f,g,h,i,j,k=this.activeIndexes,m=this.selectors=[],n=this.selectorObjects,o={},p=1===arguments.length;for(e=0,c=l(this.indexes,a);e<c.length;e++)for(d=c[e],f=k.length;f--;)if(h=k[f],d.index.isPrototypeOf(h)){if(i=h.map.get(d.key))for(g=i.length;g--;)(j=i[g]).selector===a&&(p||j.data===b)&&(i.splice(g,1),o[j.id]=!0);break}for(e in o)delete n[e],this.size--;for(e in n)m.push(n[e].selector)}},d.prototype.queryAll=function(a){if(!this.selectors.length)return[];var b,c,d,e,f,g,h,i,j={},k=[],l=this.querySelectorAll(this.selectors.join(", "),a);for(b=0,d=l.length;b<d;b++)for(c=0,f=l[b],e=(g=this.matches(f)).length;c<e;c++)j[(i=g[c]).id]?h=j[i.id]:(h={id:i.id,selector:i.selector,data:i.data,elements:[]},j[i.id]=h,k.push(h)),h.elements.push(f);return k.sort(n)},d.prototype.matches=function(a){if(!a)return[];var b,c,d,e,f,g,h,i,j,k,l,m=this.activeIndexes,o={},p=[];for(b=0,e=m.length;b<e;b++)if(i=(h=m[b]).element(a)){for(c=0,f=i.length;c<f;c++)if(j=h.map.get(i[c]))for(d=0,g=j.length;d<g;d++)!o[l=(k=j[d]).id]&&this.matchesSelector(a,k.selector)&&(o[l]=!0,p.push(k))}return p.sort(n)};var o={},p={},q=new WeakMap,r=new WeakMap,s=new WeakMap,t=Object.getOwnPropertyDescriptor(Event.prototype,"currentTarget");function u(a,b,c){var d=a[b];return a[b]=function(){return c.apply(a,arguments),d.apply(a,arguments)},a}function v(){q.set(this,!0)}function w(){q.set(this,!0),r.set(this,!0)}function x(){return s.get(this)||null}function y(a,b){t&&Object.defineProperty(a,"currentTarget",{configurable:!0,enumerable:!0,get:b||t.get})}function z(a){if(function(a){try{return a.eventPhase,!0}catch(b){return!1}}(a)){var b=(1===a.eventPhase?p:o)[a.type];if(b){var c=function(a,b,c){var d=[],e=b;do{if(1!==e.nodeType)break;var f=a.matches(e);if(f.length){var g={node:e,observers:f};c?d.unshift(g):d.push(g)}}while(e=e.parentElement)return d}(b,a.target,1===a.eventPhase);if(c.length){u(a,"stopPropagation",v),u(a,"stopImmediatePropagation",w),y(a,x);for(var d=0,e=c.length;d<e&&!q.get(a);d++){var f=c[d];s.set(a,f.node);for(var g=0,h=f.observers.length;g<h&&!r.get(a);g++)f.observers[g].data.call(f.node,a)}s.delete(a),y(a)}}}}function A(a,b,c){var e=arguments.length>3&& void 0!==arguments[3]?arguments[3]:{},f=!!e.capture,g=f?p:o,h=g[a];h||(h=new d,g[a]=h,document.addEventListener(a,z,f)),h.add(b,c)}function B(a,b,c){return a.dispatchEvent(new CustomEvent(b,{bubbles:!0,cancelable:!0,detail:c}))}},14840(a,b,c){c.d(b,{Z:()=>t});let d="data-close-dialog",e=`[${d}]`;function f(a){let b=Array.from(a.querySelectorAll("[autofocus]")).filter(h)[0];b||(b=a,a.setAttribute("tabindex","-1")),b.focus()}function g(a){let b=a.currentTarget;b instanceof Element&&("Escape"===a.key||"Esc"===a.key?(o(b,!1),a.stopPropagation()):"Tab"===a.key&&j(a))}function h(a){return a.tabIndex>=0&&!a.disabled&&i(a)}function i(a){return!a.hidden&&(!a.type||"hidden"!==a.type)&&(a.offsetWidth>0||a.offsetHeight>0)}function j(a){if(!(a.currentTarget instanceof Element))return;let b=a.currentTarget.querySelector("details-dialog");if(!b)return;a.preventDefault();let c=Array.from(b.querySelectorAll("*")).filter(h);if(0===c.length)return;let d=a.shiftKey?-1:1,e=b.getRootNode(),f=b.contains(e.activeElement)?e.activeElement:null,g=-1===d?-1:0;if(f instanceof HTMLElement){let i=c.indexOf(f);-1!==i&&(g=i+d)}g<0?g=c.length-1:g%=c.length,c[g].focus()}function k(a){let b=a.querySelector("details-dialog");return!(b instanceof DetailsDialogElement)||b.dispatchEvent(new CustomEvent("details-dialog-close",{bubbles:!0,cancelable:!0}))}function l(a){if(!(a.currentTarget instanceof Element))return;let b=a.currentTarget.closest("details");b&&b.hasAttribute("open")&&!k(b)&&(a.preventDefault(),a.stopPropagation())}function m(a){let b=a.currentTarget;if(!(b instanceof Element))return;let c=b.querySelector("details-dialog");if(c instanceof DetailsDialogElement){if(b.hasAttribute("open")){let d="getRootNode"in c?c.getRootNode():document;d.activeElement instanceof HTMLElement&&s.set(c,{details:b,activeElement:d.activeElement}),f(c),b.addEventListener("keydown",g)}else{for(let e of c.querySelectorAll("form"))e.reset();let h=n(b,c);h&&h.focus(),b.removeEventListener("keydown",g)}}}function n(a,b){let c=s.get(b);return c&&c.activeElement instanceof HTMLElement?c.activeElement:a.querySelector("summary")}function o(a,b){b!==a.hasAttribute("open")&&(b?a.setAttribute("open",""):k(a)&&a.removeAttribute("open"))}function p(a){let b=a.currentTarget;if(!(b instanceof Element))return;let c=b.querySelector("details-dialog");if(!(c instanceof DetailsDialogElement))return;let d=c.querySelector("include-fragment:not([src])");if(!d)return;let e=c.src;null!==e&&(d.addEventListener("loadend",()=>{b.hasAttribute("open")&&f(c)}),d.setAttribute("src",e),r(b))}function q(a,b,c){r(a),b&&a.addEventListener("toggle",p,{once:!0}),b&&c&&a.addEventListener("mouseover",p,{once:!0})}function r(a){a.removeEventListener("toggle",p),a.removeEventListener("mouseover",p)}let s=new WeakMap;class DetailsDialogElement extends HTMLElement{static get CLOSE_ATTR(){return d}static get CLOSE_SELECTOR(){return e}constructor(){super(),s.set(this,{details:null,activeElement:null}),this.addEventListener("click",function({target:a}){if(!(a instanceof Element))return;let b=a.closest("details");b&&a.closest(e)&&o(b,!1)})}get src(){return this.getAttribute("src")}set src(a){this.setAttribute("src",a||"")}get preload(){return this.hasAttribute("preload")}set preload(a){a?this.setAttribute("preload",""):this.removeAttribute("preload")}connectedCallback(){this.setAttribute("role","dialog"),this.setAttribute("aria-modal","true");let a=s.get(this);if(!a)return;let b=this.parentElement;if(!b)return;let c=b.querySelector("summary");c&&(c.hasAttribute("role")||c.setAttribute("role","button"),c.addEventListener("click",l,{capture:!0})),b.addEventListener("toggle",m),a.details=b,q(b,this.src,this.preload)}disconnectedCallback(){let a=s.get(this);if(!a)return;let{details:b}=a;if(!b)return;b.removeEventListener("toggle",m),r(b);let c=b.querySelector("summary");c&&c.removeEventListener("click",l,{capture:!0}),a.details=null}toggle(a){let b=s.get(this);if(!b)return;let{details:c}=b;c&&o(c,a)}static get observedAttributes(){return["src","preload"]}attributeChangedCallback(){let a=s.get(this);if(!a)return;let{details:b}=a;b&&q(b,this.src,this.preload)}}let t=DetailsDialogElement;window.customElements.get("details-dialog")||(window.DetailsDialogElement=DetailsDialogElement,window.customElements.define("details-dialog",DetailsDialogElement))}}])
//# sourceMappingURL=vendors-node_modules_delegated-events_dist_index_js-node_modules_github_details-dialog-elemen-63debe-eb36e6ab4cfc.js.map