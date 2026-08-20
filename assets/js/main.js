(function () {
  "use strict";

  /* ---------- theme ---------- */
  var root = document.documentElement;
  var stored = null;
  try { stored = localStorage.getItem("theme"); } catch (e) {}
  if (stored === "light" || stored === "dark") root.setAttribute("data-theme", stored);

  function currentTheme() {
    return root.getAttribute("data-theme") ||
      (window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.getElementById("theme-toggle");
    if (toggle) {
      toggle.addEventListener("click", function () {
        var next = currentTheme() === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try { localStorage.setItem("theme", next); } catch (e) {}
      });
    }

    /* ---------- mobile nav ---------- */
    var navToggle = document.getElementById("nav-toggle-btn");
    var navLinks = document.getElementById("nav-links");
    if (navToggle && navLinks) {
      navToggle.addEventListener("click", function () {
        navToggle.classList.toggle("is-open");
        navLinks.classList.toggle("is-open");
      });
      navLinks.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", function () {
          navToggle.classList.remove("is-open");
          navLinks.classList.remove("is-open");
        });
      });
    }

    /* ---------- active nav link on scroll ---------- */
    var sections = Array.prototype.slice.call(document.querySelectorAll("section[id]"));
    var navAnchors = Array.prototype.slice.call(document.querySelectorAll(".nav-links a"));
    if (sections.length && navAnchors.length) {
      var spy = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            navAnchors.forEach(function (a) {
              a.classList.toggle("is-active", a.getAttribute("href") === "#" + entry.target.id);
            });
          }
        });
      }, { rootMargin: "-40% 0px -50% 0px" });
      sections.forEach(function (s) { spy.observe(s); });
    }

    /* ---------- scroll reveal ---------- */
    var revealEls = Array.prototype.slice.call(document.querySelectorAll(".reveal"));
    if ("IntersectionObserver" in window && revealEls.length) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12 });
      revealEls.forEach(function (el) { io.observe(el); });
    } else {
      revealEls.forEach(function (el) { el.classList.add("is-visible"); });
    }

    /* ---------- back to top ---------- */
    var backBtn = document.getElementById("back-to-top");
    if (backBtn) {
      window.addEventListener("scroll", function () {
        backBtn.classList.toggle("is-visible", window.scrollY > 600);
      });
      backBtn.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: "smooth" });
      });
    }

    /* ---------- write-up filter ---------- */
    var filterBtns = Array.prototype.slice.call(document.querySelectorAll(".filter-btn"));
    var postCards = Array.prototype.slice.call(document.querySelectorAll(".post-card"));
    if (filterBtns.length && postCards.length) {
      filterBtns.forEach(function (btn) {
        btn.addEventListener("click", function () {
          filterBtns.forEach(function (b) { b.classList.remove("is-active"); });
          btn.classList.add("is-active");
          var cat = btn.getAttribute("data-cat");
          postCards.forEach(function (card) {
            var show = cat === "all" || card.getAttribute("data-cat") === cat;
            card.style.display = show ? "" : "none";
          });
        });
      });
    }

    /* ---------- terminal typing effect ---------- */
    var term = document.getElementById("terminal-body");
    if (term) {
      var script = [
        { type: "cmd", text: "whoami" },
        { type: "out", text: "brian_karaba_wachira" },
        { type: "cmd", text: "cat role.txt" },
        { type: "out", text: "Offensive Security Practitioner" },
        { type: "cmd", text: "cat focus.txt" },
        { type: "out", text: "Pentesting · Red Teaming · Incident Response" },
        { type: "cmd", text: "geoip --self" },
        { type: "out", text: "location: Kenya" },
        { type: "cmd", text: "cat status.txt" },
        { type: "out", text: "open to internships & offensive security work" }
      ];

      var lineEl = null;
      var li = 0, ci = 0;

      function typeNext() {
        if (li >= script.length) {
          var doneCursor = document.createElement("span");
          doneCursor.className = "cursor";
          term.appendChild(doneCursor);
          return;
        }
        var item = script[li];
        if (ci === 0) {
          lineEl = document.createElement("div");
          lineEl.className = "term-line";
          var prompt = document.createElement("span");
          prompt.className = "prompt";
          prompt.textContent = item.type === "cmd" ? "brian@offsec:~$ " : "";
          lineEl.appendChild(prompt);
          var span = document.createElement("span");
          span.className = item.type === "cmd" ? "cmd" : "out";
          lineEl.appendChild(span);
          term.appendChild(lineEl);
        }
        var span2 = lineEl.querySelector(item.type === "cmd" ? ".cmd" : ".out");
        if (ci < item.text.length) {
          span2.textContent += item.text.charAt(ci);
          ci++;
          setTimeout(typeNext, item.type === "cmd" ? 34 : 12);
        } else {
          ci = 0;
          li++;
          setTimeout(typeNext, item.type === "cmd" ? 220 : 380);
        }
      }

      var termObserved = false;
      var termIO = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting && !termObserved) {
            termObserved = true;
            setTimeout(typeNext, 350);
          }
        });
      }, { threshold: 0.3 });
      termIO.observe(term);
    }
  });
})();
