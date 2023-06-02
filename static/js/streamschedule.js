class LiveCountDown {
    /**
     Creates and renders the time left untill the next stream in real time, based on data passed from
     the static file twitchdev.ics by home.py view.
     */
    constructor() {
        this.nextStreamStamp = 0;
        this.importedTimes = dailyHours;
        this.calendar = [];
        this.now = Date.now();
        let currentWeekDay = new Date(this.now).getDay(); // integer
        let nowH = new Date(this.now).getHours();
        let nowMin = new Date(this.now).getMinutes();
        let nowSec = new Date(this.now).getSeconds();
        this.weekNowSecStamp = currentWeekDay * 24 * 3600 + (nowH * 3600 + nowMin * 60 + nowSec);
        this.clockDiv = document.querySelector('.schedule-timer');
    }

    buildCalendarStamps() {
        for (let segment of this.importedTimes) {
            let stamp = segment.day * 24 * 3600 + segment.time.split(':')[0] * 3600 + segment.time.split(':')[1] * 60;
            this.calendar.push(stamp);
        }
    }

    setNextStream() {
        for (let segment of this.calendar) {
            if (segment > this.weekNowSecStamp) {
                this.nextStreamStamp = segment - this.weekNowSecStamp;
                break;
            }
        }
        if (this.weekNowSecStamp >= this.calendar[this.calendar.length - 1]) {
            this.nextStreamStamp = this.calendar[0] + 24 * 7 * 3600 - this.weekNowSecStamp;
        }
    }

    renderClock() {
        let stamp = this.nextStreamStamp;
        let seconds = stamp % 60 % 60;
        let minutes = Math.floor(stamp / 60 % 60);
        let hours = Math.floor(stamp / 60 / 60);
        let localeH = hours.toLocaleString('en-US', {
            minimumIntegerDigits: 2,
            useGrouping: false
        });
        let localeM = minutes.toLocaleString('en-US', {
            minimumIntegerDigits: 2,
            useGrouping: false
        });
        let localeS = seconds.toLocaleString('en-US', {
            minimumIntegerDigits: 2,
            useGrouping: false
        });
        this.clockDiv.textContent = `${localeH}: ${localeM}: ${localeS}`;
    }
}

function main() {
    let countdownState = new LiveCountDown();
    countdownState.buildCalendarStamps();
    countdownState.setNextStream();
    countdownState.renderClock();
    setTimeout(main, 1000);
}

main();