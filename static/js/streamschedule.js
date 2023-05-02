
let weekdays=new Array(7);
weekdays[0]="Sunday";
weekdays[1]="Monday";
weekdays[2]="Tuesday";
weekdays[3]="Wednesday";
weekdays[4]="Thursday";
weekdays[5]="Friday";
weekdays[6]="Saturday";


class LiveCountDown{
    constructor(){
        this.now = Date.now()
        this.currentWeekDay = new Date(this.now).getDay() // integer
        this.todayString = weekdays[this.currentWeekDay]
        this.tomorrowString = this.currentWeekDay < 7 ? weekdays[this.currentWeekDay+1] : weekdays[0]

        this.todayStream = dailyHours[this.todayString]
        this.tomorrowStream = dailyHours[this.tomorrowString]

        this.streamStartHour =  Number(this.todayStream.split(':')[0])
        this.streamStartMin =   Number(this.todayStream.split(':')[1])
        this.tomorrowStreamStartH = Number(this.tomorrowStream.split(':')[0])
        this.tomorrowStreamStartM = Number(this.tomorrowStream.split(':')[1])

        this.nowH = new Date(this.now).getHours()
        this.nowMin = new Date(this.now).getMinutes()
        this.nowSec = new Date(this.now).getSeconds()

        this.countdown = {
            H : this.streamStartHour - this.nowH,
            M : this.streamStartMin - this.nowMin,
            S : this.nowSec,
        }
        this.clockDiv = document.querySelector('.schedule-timer') // timer container
    }

    liveClock(){
        if (this.countdown['S'] <= 0){
            this.countdown['S'] += 60
            this.countdown['M'] -= 1
        }
        if (this.countdown['M'] <= 0){
            this.countdown['M'] += 60
            this.countdown['H'] -= 1
        }
        if (this.countdown['H'] < 0){
            this.countdown['H'] = 24 - this.nowH + this.tomorrowStreamStartH
            this.countdown['M'] = this.tomorrowStreamStartM - this.nowMin
            this.liveClock()
        }
        this.countdown['S'] -= 1
    }

    renderClock(){
        let localeH = this.countdown.H.toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})
        let localeM = this.countdown.M.toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})
        let localeS = this.countdown.S.toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping:false})
        this.clockDiv.textContent = `${localeH}: ${localeM}: ${localeS}`
    }
}
let countdownState = new LiveCountDown()

function main(){
    countdownState.liveClock()
    countdownState.renderClock()
    setTimeout(main, 1000)

}

main()



