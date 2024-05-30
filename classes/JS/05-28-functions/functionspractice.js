function time(hrs = "00", mins = "00", secs = "00") {
    if (mins < 10) {
        mins = "0" + mins;
    }
    if (hrs < 10) {
        hrs = "0" + hrs;
    }
    if (secs < 10) {
        hrs = "0" + secs;
    }
    if (mins > 60) {
        hrs = hrs + 1;
        mins = "00";
    }
    
    return `${hrs}:${mins}:${secs}`;

}

function toSeconds(hrs = 0, mins = 0, secs = 0) {
    let hrsToSec = hrs * 3600;
    let minsToSec = mins * 60;
    let total = hrsToSec + minsToSec + secs;
    return total;
}

function toTime (secs) {
    let toHours = Math.floor(secs / 3600);
    secs = secs - toHours * 3600;
    let toMinutes = Math.floor(secs / 60);
    secs = secs - toMinutes * 60;
    let toSeconds = secs % 60;
    let total = `${toHours}:${toMinutes}:${toSeconds}`;
    return total;
}   


function deltaTime (h1, m1, s1, h2, m2, s2) {
    let firstTime = toSeconds(h1, m1, s1);
    let secondTime = toSeconds(h2, m2, s2);
    let delta = firstTime - secondTime;
    if (delta < 0) {
        delta = -delta;
    }
    let result = toTime(delta);
    return result;
}