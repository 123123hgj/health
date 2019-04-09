$(function () {
    for (var i = 1; i <= 9; i++) {
        new scale('btn' + i, 'bar' + i, 'title' + i); //实例化一个拖拽
    }

    function inputcsh() {
        $('input').iCheck({
            checkboxClass: 'icheckbox_square-blue',
            radioClass: 'iradio_square-blue',
            increaseArea: '20%', // optional
            labelHover: true,
        });
    }

    inputcsh();
    var tt_num = 0;
    $("#add_bz").click(function () {

        var html = '<div class="row"> ' +
            '   <div class="col-sm-12"> ' +
            '       <div class="checkbox input-group"> ' +
            '           <div class="col-sm-2"> ' +
            '             <input type="checkbox" checked /> ' +
            '             <input type="text"  class="form-control2" placeholder="Input symptoms"  /> ' +
            '            </div> ' +
            '            <div class="col-sm-2 btn-group"> ' +
            '             <select name="dataTable_length" aria-controls="dataTable" class="custom-select form-control"> <option value="0">Duration of symptoms</option> <option value="morning">morning</option><option value="at noon">at noon</option><option value="afternoon">afternoon</option><option value="evening">evening</option><option value="other">other</option> </select> ' +
            '            </div> ' +
            '            <div class="input-group col-sm-2"> ' +
            '             <input type="text" class="form-control" placeholder="Fill in the parts"  /> ' +
            '            </div> ' +
            '            <div class="input-group col-sm-4"> ' +
            '              <label class="col-sm-4 linh">pain degree：<span id="ntitle' + tt_num + '">0</span></label>' +
            '              <div class="scale col-sm-4" id="nbar' + tt_num + '">' +
            '                  <div></div>' +
            '                  <span id="nbtn' + tt_num + '"></span>' +
            '              </div>' +
            '         </div> ' +
            '      </div> ' +
            '   </div>' +
            '   <div class="clearfix" style="margin-bottom: 10px;"></div>';
        $("#brappenddiv").append(html);
        new scale('nbtn' + tt_num, 'nbar' + tt_num, 'ntitle' + tt_num);

        tt_num++;
        inputcsh();

    })

});
$(function () {
    $('#datetimepicker1').datetimepicker({
        format: 'YYYY-MM-DD',
        minDate: new Date(),
    });
});