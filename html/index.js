(function() {
  "use strict";

  window.addEventListener("load", initialize);

  function initialize() {
    $("submit-button").addEventListener("click", switchViews);
    $("start-button").addEventListener("click" , switchViews);
    $("to-download").addEventListener("click" , switchViews);
    $("to-login").addEventListener("click" , switchViews);
    $("to-flag").addEventListener("click" , switchViews);
    $("flag-back").addEventListener("click", switchViews);
    $("download-back").addEventListener("click", switchViews);
    $("login-back").addEventListener("click", switchViews);
  }

  function portHandler() {

  }

  function downloadHandler() {

  }

  function loginHandler() {

  }

  function flagHandler() {

  }

//Function to switch views
  function switchViews() {
    var currentView = "";
    var nextView = "";
    if(this.id == "start-button") {
      currentView = "home";
      nextView = "port";
      qs("h1").classList.add("hidden");
    } else if (this.id == "submit-button") {
      currentView = "port";
      nextView = "menu";
      qs("h2").classList.remove("hidden");
    } else if (this.id == "to-download") {
      currentView = "menu";
      nextView = "download";
      qs("h2").innerText = "Click to download the pcap file";
      qs("h2").classList.remove("pick-challenge");
    } else if (this.id == "to-login") {
      currentView = "menu";
      nextView = "login";
      qs("h2").classList.add("hidden");
    } else if (this.id == "to-flag") {
      currentView = "menu";
      nextView = "flag";
      qs("h2").classList.add("hidden");
    } else if (this.id == "flag-back") {
      currentView = "flag";
      nextView = "menu";
      qs("h2").classList.remove("hidden");
    } else if (this.id == "download-back") {
      currentView = "download";
      nextView = "menu";
      qs("h2").innerText = "Pick your challenge!";
      qs("h2").classList.add("pick-challenge");
      qs("h2").classList.remove("hidden");
    } else if (this.id == "login-back") {
      currentView = "login";
      nextView = "menu";
      qs("h2").classList.remove("hidden");
    }

    $(currentView).classList.add("hidden");
    $(nextView).classList.remove("hidden");
  }

  //Helper function to simplify calling a single element.
  function $(id) {
    return document.getElementById(id);
  }

  //Helper function to simplify calling multiple elements.
  function qsa(query) {
    return document.querySelectorAll(query);
  }

  //Helper function to simplify calling a class or semantic element.
  function qs(query) {
    return document.querySelector(query);
  }
})();
