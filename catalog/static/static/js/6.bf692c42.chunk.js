(this["webpackJsonp@coreui/coreui-free-react-admin-template"]=this["webpackJsonp@coreui/coreui-free-react-admin-template"]||[]).push([[6],{623:function(e,t,a){"use strict";a.d(t,"d",(function(){return r})),a.d(t,"a",(function(){return o})),a.d(t,"b",(function(){return i})),a.d(t,"c",(function(){return c})),a.d(t,"e",(function(){return u}));var n=a(624),l=a.n(n);function r(e){var t="/catalog/api/books/";return t=function(e,t){var a="https://"+window.location.host+e;console.log(a);var n=new URL(a);return Object.keys(t).forEach((function(e){n.searchParams.append(e,t[e])})),n}(t,e),fetch(t).then((function(e){return e.json()}))}function c(e){return fetch("/catalog/api/books/"+e).then((function(e){return e.json()}))}function o(e){var t={method:"POST",body:JSON.stringify(e),headers:{"Content-Type":"application/json","X-CSRFTOKEN":l.a.get("csrftoken")}};return fetch("/catalog/api/books/",t).then((function(e){return e.json()}))}function u(e){var t="/catalog/api/books/"+e.id+"/",a={method:"PUT",body:JSON.stringify(e),headers:{"Content-Type":"application/json","X-CSRFTOKEN":l.a.get("csrftoken")}};return fetch(t,a).then((function(e){return e.json()}))}function i(){return fetch("/catalog/api/authors/").then((function(e){return e.json()})).then((function(e){return e.map((function(e){return e.value=e.id,e.key=e.id,e.label=e.first_name+" "+e.last_name,e}))}))}},648:function(e,t,a){"use strict";a.r(t);var n=a(621),l=a.n(n),r=a(622),c=a(617),o=a(1),u=a.n(o),i=a(19),s=a(637),m=a(638),h=function(e){var t=e.options,a=e.children,n=e.maxHeight,l=(0,e.getValue)(),r=Object(c.a)(l,1)[0],o=35*t.indexOf(r);return u.a.createElement(m.a,{height:n,itemCount:a.length,itemSize:35,initialScrollOffset:o},(function(e){var t=e.index,n=e.style;return u.a.createElement("div",{style:n},a[t])}))},E=a(616),p=a(615),d=a(623);t.default=function(e){var t=Object(i.h)(),a=Object(o.useState)({title:"",titleShort:"",isbn:"",callNumber:"",language:"",pages:"",publisher:"",publisherPlace:"",issued:"",collectionTitle:"",place:"",abstract:""}),n=Object(c.a)(a,2),m=n[0],b=n[1],f=Object(o.useState)([]),g=Object(c.a)(f,2),v=g[0],O=g[1],j=Object(o.useState)([]),C=Object(c.a)(j,2),S=C[0],k=C[1];function y(e){var t=e.target.id,a=e.target.value,n=JSON.parse(JSON.stringify(m));n[t]=a,b(n)}return Object(o.useEffect)((function(){!function(){var e=Object(r.a)(l.a.mark((function e(){var a,n,r,o,u,i;return l.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(!t.id){e.next=13;break}return e.next=3,Promise.all([Object(d.b)(),Object(d.c)(t.id)]);case 3:a=e.sent,n=Object(c.a)(a,2),r=n[0],o=n[1],b(o),O(r),u=r.filter((function(e){return o.author.includes(e.id)})),k(u),e.next=17;break;case 13:return e.next=15,Object(d.b)();case 15:i=e.sent,O(i);case 17:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}()()}),[t]),u.a.createElement(u.a.Fragment,null,u.a.createElement(E.I,null,u.a.createElement(E.j,null,u.a.createElement(E.e,null,u.a.createElement(E.i,null,"Create Book"),u.a.createElement(E.f,null,u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"title"},"Authors"),u.a.createElement(s.a,{components:{MenuList:h},onChange:function(e){k(e)},value:S,options:v,isMulti:!0})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"title"},"Title"),u.a.createElement(E.z,{id:"title",placeholder:"Book title",onChange:y,value:m.title||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"titleShort"},"Short Title"),u.a.createElement(E.z,{id:"titleShort",placeholder:"Short title",onChange:y,value:m.titleShort||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"isbn"},"ISBN"),u.a.createElement(E.z,{id:"isbn",placeholder:"978-1-86197-876-9",onChange:y,value:m.isbn||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"callNumber"},"Call Number"),u.a.createElement(E.z,{id:"callNumber",placeholder:"",onChange:y,value:m.callNumber||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"language"},"Language"),u.a.createElement(E.z,{id:"language",placeholder:"es",onChange:y,value:m.language||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"pages"},"Pages"),u.a.createElement(E.z,{id:"pages",placeholder:"",onChange:y,value:m.pages||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"publisher"},"Publisher"),u.a.createElement(E.z,{id:"publisher",placeholder:"",onChange:y,value:m.publisher||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"publisherPlace"},"Publisher Place"),u.a.createElement(E.z,{id:"publisherPlace",placeholder:"",onChange:y,value:m.publisherPlace||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"issued"},"Issued"),u.a.createElement(E.z,{id:"issued",placeholder:"",onChange:y,value:m.issued||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"collectionTitle"},"Collection Title"),u.a.createElement(E.z,{id:"collectionTitle",placeholder:"",onChange:y,value:m.collectionTitle||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"place"},"Place"),u.a.createElement(E.z,{id:"place",placeholder:"",onChange:y,value:m.place||""})),u.a.createElement(E.u,null,u.a.createElement(E.E,{htmlFor:"abstract"},"Abstract"),u.a.createElement(E.R,{name:"abstract",id:"abstract",rows:"10",placeholder:"Content...",onChange:y,value:m.abstract||""}))),u.a.createElement(E.g,null,u.a.createElement("span",{className:"mr-2"},u.a.createElement(E.d,{type:"submit",size:"sm",color:"primary",onClick:function(){m.author=S.map((function(e){return e.key})),t.id?Object(d.e)(m).then((function(e){console.log(e)})):Object(d.a)(m).then((function(e){console.log(e)}))}},u.a.createElement(p.a,{name:"cil-scrubber"})," Submit")),u.a.createElement(E.d,{type:"reset",size:"sm",color:"danger",onClick:function(){console.log("test")}},u.a.createElement(p.a,{name:"cil-ban"})," Reset"))))))}}}]);
//# sourceMappingURL=6.bf692c42.chunk.js.map