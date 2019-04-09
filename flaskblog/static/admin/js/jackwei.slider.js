var scale = function (btn,bar,title){
    this.btn = document.getElementById(btn);
    this.bar = document.getElementById(bar);
    this.title = document.getElementById(title);
    this.step = this.bar.getElementsByTagName("div")[0];
 
    
    if ((navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i))) {
            this.init = function (){
                var f=this,g=document,b=window,m=Math;
                f.btn.ontouchstart=function (e){

                    var x=e.touches[0].pageX;
                    var l=this.offsetLeft;
                    console.log(e.touches[0].pageX)
                    var max=f.bar.offsetWidth-this.offsetWidth;
                    g.ontouchmove=function (e){
                        var thisX=(e||b.event).clientX;
                        var to=m.min(max,m.max(-2,l+(thisX-x)));
                        f.btn.style.left=to+'px';
                        f.ondrag(m.round(m.max(0,to/max)*10),to);
                        b.getSelection ? b.getSelection().removeAllRanges() : g.selection.empty();
                    };
                    g.ontouchend=new Function('this.onmousemove=null');
                };
            };
    }else{
        this.init = function (){
            var f=this,g=document,b=window,m=Math;
            f.btn.onmousedown=function (e){
                var x=(e||b.event).clientX;
                var l=this.offsetLeft;
                var max=f.bar.offsetWidth-this.offsetWidth;
                g.onmousemove=function (e){
                    var thisX=(e||b.event).clientX;
                    var to=m.min(max,m.max(-2,l+(thisX-x)));
                    f.btn.style.left=to+'px';
                    f.ondrag(m.round(m.max(0,to/max)*10),to);
                    b.getSelection ? b.getSelection().removeAllRanges() : g.selection.empty();
                };
                g.onmouseup=new Function('this.onmousemove=null');
            };
        };
    }
    this.ondrag = function (pos,x){
        this.step.style.width=Math.max(0,x)+'px';
        this.title.innerHTML=pos;
    };
    this.init();
}