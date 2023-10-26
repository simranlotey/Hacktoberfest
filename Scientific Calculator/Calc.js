function display(text)
{
    var output = document.getElementById("display");
    output.value += text;
    document.getElementById("display").focus();
}
function remove() 
{
    var output = document.getElementById("display");
    var outputVal = output.value;
    var length = outputVal.length;
    outputVal = outputVal.substring(0, length - 1);
    output.value = outputVal;
    document.getElementById("display").focus();
}
function clearAll()
{
    var output = document.getElementById("display");
    output.value = "";
    document.getElementById("display").focus();
}
function compute()
{
    var output = document.getElementById("display");
    var val= output.value;
    if(val === "69*420")
        window.location.href = "https://www.youtube.com/watch?v=xvFZjo5PgG0";
    val.includes("sin") ? val = val.replace("sin", "Math.sin") : val;
    val.includes("cos") ? val = val.replace("cos", "Math.cos") : val;
    val.includes("tan") ? val = val.replace("tan", "Math.tan") : val;
    val.includes("log") ? val = val.replace("log", "Math.log10") : val;
    val.includes("sqrt") ? val = val.replace("sqrt", "Math.sqrt") : val;
    val.includes("PI") ? val = val.replace("PI", "Math.PI") : val;
    val.includes("e") ? val = val.replace("e", "Math.E") : val;
    val.includes("ln") ? val = val.replace("ln", "Math.log") : val;
    val.includes("^") ? val = val.replace("^", "**") : val;
    val.includes("e^") ? val = val.replace("e^", "Math.exp") : val;
    try{
        output.value = eval(val).toFixed(8);
        document.getElementById("display").focus();
        if(output.value == "Infinity")
            output.value = "Value Error";
    }
    catch(err){
        output.value = "Error";
    }

}
function execute(event)
{
    if(event.key === "Enter")
        compute();
}
