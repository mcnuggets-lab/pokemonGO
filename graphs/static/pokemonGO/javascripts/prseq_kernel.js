// Form processing
var prime = 2543;
var seqLength = 16;
var code = '';

$(document).ready(function () {
    $("#btnreset").click(function () {
        reset();
    });
});

function reset() {
    prime = 2543;
    seqLength = 16;
    code = '';
    $("#inputp").val('2543');
    $("#inputl").val('16');
    $("#display").html('The generator has been reset.');
}



$("#formPR").on("submit", function (e) {
    e.preventDefault();
    $("#genPR").attr("disabled", "disabled");
    $("#genPR").css("color", "grey");
    if (prime != $("#inputp").val() || seqLength != $("#inputl").val()) {
        code = '';
        prime = $("#inputp").val();
        seqLength = $("#inputl").val();
    }

    $.post(
        "/maths/PRseq/run",
        { inputp: $("#inputp").val(), inputl: $("#inputl").val() },
        function (responseText) {
            if (responseText.err) {
                code = '';
                $("#display").html(responseText.err);
            }
            else {
                code += responseText.output + '<br />';
                $("#display").html(code);
            }
            $("#genPR").removeAttr("disabled");
            $("#genPR").css("color", "inherit");
        }
    );
});




