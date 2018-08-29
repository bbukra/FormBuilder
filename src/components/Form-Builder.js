export default 
{
    name: 'Form_Builder'
}

function add_Field()
{
    // console.log("Hello Blat");
    var para = document.createElement("p");
    var node = document.createTextNode("This is new.");
    para.appendChild(node);

    var element = document.getElementById("div1");
    var child = document.getElementById("p1");
    element.insertBefore(para, child);


    // var para = document.createElement("br");
    // var node = document.createTextNode("This is new.");
    // para.appendChild(node);
    // var AddFieldButton = document.getElementById("AddFieldButton");
    // var Form_Builder_Page = document.getElementById("Form_Builder_Page");
    // Form_Builder_Page.insertBefore(para, AddFieldButton)
    // var new_Field = document.createElement("input type=\"text\"");
}