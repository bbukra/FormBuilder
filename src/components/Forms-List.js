//import Forms_List from './Forms-List'
export default {
    name: 'Forms-List'
}
var form_id = 1;
function insRow(form_Name)
{
    
    var x=document.getElementById('Forms_List_Table').insertRow(1);
    var c1=x.insertCell(0);
    var c2=x.insertCell(1);
    var c3=x.insertCell(2);
    var c4=x.insertCell(3);
    var c5=x.insertCell(4);

    c1.innerHTML= form_id;
    c2.innerHTML= form_Name;

    form_id++; //advance the counter of form id
}
