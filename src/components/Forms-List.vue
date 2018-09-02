<template>
    <html>
        <body>
            <table id="Forms_List_Table">
                <tr>
                    <th>Form Id</th>
                    <th>Form Name</th> 
                    <th># Submissions</th>
                    <th>Submit Page</th>
                    <th>Submissions Page</th>
                </tr>            
            </table>
            <br>
            <form action="/Form-Builder">
                <input type="submit" id="New_Form_Button" value="Create a new form" />
            </form>
        </body>
    </html>
</template>

<script>
import Vue from "vue";


export default 
{
    name: 'Forms_List',  
    data() 
    {
        return {
        }
    },
    created : function () 
    {
        this.get_Forms_List_From_DB();
    }
    ,
    methods: 
    {
        get_Forms_List_From_DB: function() 
        {
            var forms_Names = '';
            var forms_Names_Array = [];
            this.$http.get('http://localhost:5000/get_Forms_List', "", {
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Access-Control-Allow-Origin': 'http://localhost:8080'
            }
            }).then( response => {
                forms_Names_Array = response.data,
                this.display_All_Forms(forms_Names_Array)
              })
        }
        ,
        display_All_Forms: function(forms_Names_Array)
        {
            var Forms_List_Table = document.getElementById("Forms_List_Table")
            var idx;
            for (idx = 0; idx < forms_Names_Array.length ; idx++)
            {
                this.insertRow(forms_Names_Array[idx].FormName, forms_Names_Array[idx].id);
            }

        }
        ,
        insertRow: function(curr_Form_Name, form_id)
        {
            var new_Row = document.getElementById('Forms_List_Table').insertRow(form_id);
            var form_Id_Col = new_Row.insertCell(0);
            var form_Name_Col = new_Row.insertCell(1);
            var count_Submissions_Col = new_Row.insertCell(2);
            var submit_Page_Col = new_Row.insertCell(3);
            var sumbissions_Page_Col = new_Row.insertCell(4);

            form_Id_Col.innerHTML= form_id;
            form_Name_Col.innerHTML= curr_Form_Name;
            count_Submissions_Col.innerHTML= "# Submissions:TBD";

            var button_Properties;
            var view_Submit_Page_Button = document.createElement("form");
            view_Submit_Page_Button.setAttribute("action", "/Submit-Page/" + form_id.toString());
            button_Properties = view_Submit_Page_Button.appendChild(document.createElement("input"));
            button_Properties.setAttribute("type", "submit");
            button_Properties.setAttribute("value", "View");
            submit_Page_Col.appendChild(view_Submit_Page_Button);

            var view_Submissions_Page_Button = document.createElement("form");
            view_Submissions_Page_Button.setAttribute("action", "/Submissions-Page/" + form_id.toString());
            button_Properties = view_Submissions_Page_Button.appendChild(document.createElement("input"));
            button_Properties.setAttribute("type", "submit");
            button_Properties.setAttribute("value", "View");
            sumbissions_Page_Col.appendChild(view_Submissions_Page_Button);
        }
        ,
        SubmitPage: function() 
        {
            console.log(form_id);
            // window.location='/Submit-Page?form_id='+form_id.toString();
        }
        ,
        SubmissionsPage: function(form_id)
        {
            // window.location='/Submissions-Page?form_id='+form_id.toString();
        }
    }
    
}
</script>
<style src="./Forms-List.css"></style>
