// ==UserScript==
// @name         StackOverFlowScriptAddButtons
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You

// @grant        none
// @include https://stackoverflow.com/*
// @require http://code.jquery.com/jquery-latest.js
// @require https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js
// ==/UserScript==

var node;
var n;

var tags=["code-error","system-crash","discrepancy","implementation","conceptual"];

$(document).ready(function() {
  alert('STARTED!!!');
      var int = 0;

    for (int = 0; int < 10; int++) {
       
        node = create(tags[int]);

    var i = document.getElementsByClassName('summary')[int];
    var x = document.getElementsByClassName('summary')[int].childElementCount;
    i.insertBefore(node, i.childNodes[x+4+int]);
    
    }
    });
function create(tags){
   var node = document.createElement("a");
   node.innerHTML = tags;
    if(tags=="code-error" || tags == "system-crash"){
   node.setAttribute("href", "/questions/tagged/"+tags);
   node.setAttribute("class","btn btn-warning");
    }
    if(tags=="discrepancy" || tags == "implementation" || tags == "conceptual"){
   node.setAttribute("href", "/questions/tagged/"+tags);
   node.setAttribute("class","btn");
    }
    //if(tags=="discrepancy")
   //node.setAttribute("href", "/questions/tagged/"+tags);
   //node.setAttribute("class","btn btn-success");
   return node;
   }

