<template>
    <html>
        <h1>Create the Form You Want</h1>
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
                var form_id = forms_Names_Array[idx].id;
                var curr_Form_Name = forms_Names_Array[idx].FormName;
                var number_of_submissions = forms_Names_Array[idx].submissionsCount;
                this.insertRow(curr_Form_Name, form_id, number_of_submissions);
            }

        }
        ,
        insertRow: function(curr_Form_Name, form_id, number_of_submissions)
        {
            var new_Row = document.getElementById('Forms_List_Table').insertRow(form_id);
            var form_Id_Col = new_Row.insertCell(0);
            var form_Name_Col = new_Row.insertCell(1);
            var count_Submissions_Col = new_Row.insertCell(2);
            var submit_Page_Col = new_Row.insertCell(3);
            var sumbissions_Page_Col = new_Row.insertCell(4);

            form_Id_Col.innerHTML= form_id;
            form_Name_Col.innerHTML= curr_Form_Name;
            count_Submissions_Col.innerHTML= number_of_submissions;

            var button_Properties;
            var view_Submit_Page_Button = document.createElement("form");
            view_Submit_Page_Button.setAttribute("action", "/Submit-Page/" + form_id.toString());
            button_Properties = view_Submit_Page_Button.appendChild(document.createElement("input"));
            button_Properties.setAttribute("class", "link_Buttons");
            button_Properties.setAttribute("type", "submit");
            button_Properties.setAttribute("value", "View");
            submit_Page_Col.appendChild(view_Submit_Page_Button);

            var view_Submissions_Page_Button = document.createElement("form");
            view_Submissions_Page_Button.setAttribute("action", "/Submissions-Page/" + form_id.toString());
            button_Properties = view_Submissions_Page_Button.appendChild(document.createElement("input"));
            button_Properties.setAttribute("class", "link_Buttons");
            button_Properties.setAttribute("type", "submit");
            button_Properties.setAttribute("value", "View");
            sumbissions_Page_Col.appendChild(view_Submissions_Page_Button);
        }
    }
    
}
</script>

<style>
html {
    background-color: #57c2da;
}
h1 {
    color: white;
    font-family: HelveticaNeueW01-75Bold,HelveticaNeueW02-75Bold,HelveticaNeueW10-75Bold,Helvetica Neue,Arial,Helvetica,sans-serif;
    font-weight: 400;
    font-size: 6vw;
    line-height: 1.15;
    margin: 0 0 6%;
}
table {
    border-collapse: collapse;
    width: 60%;
    margin: auto;
    font-family: "HelveticaNeueW01-45Ligh",arial,sans-serif;
    color: #363636;
    font-size: 18px;
    line-height: 1.3;

}
  
  
  thead {
    color: #fff;
    border-top: 1px solid #cdcdcd;
    border-bottom: 1px solid #cdcdcd;
    font-family: helveticaneuew01-75bold,Helvetica,Arial,sans-serif;
    font-size: 14px;
    display: table-header-group;
    vertical-align: middle;
    border-color: inherit;
    line-height: 1.3;
  }

  tr:nth-of-type(2n) {
    background-color: #f1f1f1;
  }
  tr:nth-of-type(2n+1) {
    background-color: rgb(223, 223, 223);
  }
  tr:hover {
    background-color: rgb(91, 146, 248);
  }
  th, td {
    border: 1px solid black;
    padding: 10px;
    white-space: nowrap;
    text-align: center;
  }
  tr:nth-of-type(1):hover {
      background-color: rgb(223, 223, 223);
  }
.link_Buttons {
    height: 48px;
    width: 133.33333px;
    border: 0;
    box-shadow: none;
    text-align: center;
    font-family: "HelveticaNeueW01-65Medi",arial,sans-serif;
    position: relative;
    line-height: 38px;
    font-size: 16px;
    padding: 0;
    color: #fff;
    background-color: #08c;
}
.link_Buttons:hover {
    background-color: rgba(0, 136, 204, 0.774);
}
.link_Buttons:active {
    top:1px;
}

#New_Form_Button { 
    font-size: 2vw;
    color: #3182c8;
    background-color: #fff;
    font-family: HelveticaNeueW01-65Medi,HelveticaNeueW02-65Medi,HelveticaNeueW10-65Medi,Helvetica Neue,Arial,Helvetica,sans-serif;
    padding: .6em 2.1em;
    border-radius: 1.3em;
    display: inline-block;
    line-height: 1.6;
    margin: 0 0 2px;
    position: relative;
    margin-bottom: 2px;
    cursor: pointer;
    text-align: center;
    -webkit-font-smoothing: antialiased;
    font-weight: 300;
}
#New_Form_Button:hover { 
    background-color: rgb(226, 226, 226);
}
</style>
