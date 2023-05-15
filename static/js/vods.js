

for (let vod of vodsArray){
    console.log(vod)
    let options = {
        width: '100%',
        height: '100%',
        video: vod.id,
        preload: 'metadata',
        autoplay: false,
    };

    let player = new Twitch.Player(vod.id, options);
    player.setVolume(0.5);
}
