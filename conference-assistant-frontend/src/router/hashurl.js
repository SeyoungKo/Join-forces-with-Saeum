module.exports= {
    returnUrl:function(){
        var session = JSON.parse(sessionStorage.getItem("teaminfo"))
        var url = '';

        if(url === ''){
            url = 'main';
        }else{
            url = session.team_url;
        }
        return url;
    }
}