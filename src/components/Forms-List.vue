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
        insertRow: function(curr_Form_Name, index)
        {
            var new_Row = document.getElementById('Forms_List_Table').insertRow(index);
            var c1 = new_Row.insertCell(0);
            var c2 = new_Row.insertCell(1);
            var c3 = new_Row.insertCell(2);
            var c4 = new_Row.insertCell(3);
            var c5 = new_Row.insertCell(4);

            c1.innerHTML= index;
            c2.innerHTML= curr_Form_Name;
            c3.innerHTML= "# Submissions:TBD";

            var view_Submit_Page_Button = document.createElement("button");
            view_Submit_Page_Button.setAttribute("id", "SubmitPage" + index.toString());
            view_Submit_Page_Button.setAttribute("v-on:click", "SubmitPage(" + index.toString() + ")");
            view_Submit_Page_Button.appendChild(document.createTextNode('View'))
            c4.appendChild(view_Submit_Page_Button)
            
            var view_Submissions_Page_Button = document.createElement("button");
            view_Submissions_Page_Button.setAttribute("id", "SubmissionsPage" + index.toString());
            view_Submissions_Page_Button.setAttribute("v-on:click", "SubmissionsPage(" + index.toString() + ")");
            view_Submissions_Page_Button.appendChild(document.createTextNode('View'))
            c5.appendChild(view_Submissions_Page_Button)
        }
    }
    
}
</script>
<style src="./Forms-List.css"></style>
