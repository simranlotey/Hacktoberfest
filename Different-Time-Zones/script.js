function updateClock() {
    const newYorkTime = new Date().toLocaleString("en-US", {
      timeZone: "America/New_York"
    });
    const londonTime = new Date().toLocaleString("en-GB", {
      timeZone: "Europe/London"
    });
    const tokyoTime = new Date().toLocaleString("en-JP", {
      timeZone: "Asia/Tokyo"
    });
  
    document.getElementById("new-york-time").textContent = newYorkTime;
    document.getElementById("london-time").textContent = londonTime;
    document.getElementById("tokyo-time").textContent = tokyoTime;
  }
  
  updateClock();
  setInterval(updateClock, 1000);
  