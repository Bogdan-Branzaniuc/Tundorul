class LiveCountDown{
    constructor(){

        this.callendar = {}
        for (let [day, time] of Object.entries(dailyHours)){
            this.callendar[day] = {
                h: time.split(':')[0],
                m: time.split(':')[1],
                secStamp: time.split(':')[0]*3600 + time.split(':')[1]* 60
            }
        }
        for (let i = 0; i < 7; i++){
           if(!this.callendar[i]) this.callendar[i] = 'restDay'
        }

        this.now = Date.now()
        this.currentWeekDay = new Date(this.now).getDay() // integer


        this.leftOfDaySecStamp = 0
        this.nowH = new Date(this.now).getHours()
        this.nowMin = new Date(this.now).getMinutes()
        this.nowSec = new Date(this.now).getSeconds()
        this.nowSecStamp = this.nowSec + this.nowMin * 60 + this.nowH * 3600

        this.clockDiv = document.querySelector('.schedule-timer') // timer container
    }


    renderClock(){
        let totalSecStamp =  this.leftOfDaySecStamp
        let seconds = totalSecStamp%60 % 60
        let minutes = Math.floor(totalSecStamp/60 % 60)
        let hours = Math.floor(totalSecStamp/60/60)

        let localeH = hours.toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})
        let localeM = minutes.toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})
        let localeS = seconds.toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})
        this.clockDiv.textContent = `${localeH}: ${localeM}: ${localeS}`
    }

    findNextStream() {
        let searchDay = this.currentWeekDay
        for (let i = 0; i < 7; i++) {
            let calSearch = this.callendar[searchDay]
            if (calSearch == 'restDay' || this.nowSecStamp > calSearch.secStamp) {
                searchDay = searchDay+1>6? 0 : searchDay+1
                this.leftOfDaySecStamp += 24*3600 - this.nowH*3600 - this.nowMin * 60 - this.nowSec
            }else{
                this.streamStartHour = calSearch.h
                this.streamStartMin = calSearch.m
                this.leftOfDaySecStamp += calSearch.secStamp - this.nowSecStamp
                break
            }
        }
    }
}

function main(){
    let countdownState = new LiveCountDown()
    countdownState.findNextStream()
    countdownState.renderClock()
    setTimeout(main, 1000)
}

main()



