<template>
    <html>
        <h2>Form Submissions</h2>
        <body id="Submissions_Page">

        </body>
    </html>
</template>

<script>
import Vue from "vue";


export default 
{
    name: 'Submissions_Page',
    data() {
        return {
            form_id: window.location.pathname.slice("/Submissions-Page/".length)
        }
    }, 
    created : function () 
    {
        this.get_Form_Submissions();
    }
    ,
    methods: 
    {
       get_Form_Submissions: function()
       {
           var all_Submissions_Arr = [];
           var number_of_fields = 0;
           this.$http.get('http://localhost:5000/get_Form_Submissions?form_id=' + this.form_id, "", {
            headers: {
              'Accept': 'text/html',
              'Content-Type': 'text/html',
              'Access-Control-Allow-Origin': 'http://localhost:8080'
            }
            }).then( response => {
                all_Submissions_Arr = response.data,
                number_of_fields = all_Submissions_Arr[all_Submissions_Arr.length - 1], //the last elem is the number of fields
                all_Submissions_Arr = all_Submissions_Arr.slice(0, -1), //remove the number of fields elem
                this.display_All_Submissions(all_Submissions_Arr, number_of_fields)
              })
       }
       , 
       display_All_Submissions: function(all_Submissions_Arr, number_of_fields)
       {
           var TABLE_NOT_CREATED = false;
           if(this.createTableHeaders(all_Submissions_Arr, number_of_fields) == TABLE_NOT_CREATED)
           {
               window.alert("Please submit at least one form in order to see submissions list.");
               window.location ='/';
               return;
           }
           for (var i = 0; i < all_Submissions_Arr.length; i++)
           {
               this.insertRow(all_Submissions_Arr[i], number_of_fields, i + 1);
           }
       }
       ,
       insertRow: function (curr_submission, number_of_fields, submission_index)
       {
           var new_Row = document.getElementById('Submissions_Table').insertRow(submission_index);
           var submission_number = new_Row.insertCell(0);
           submission_number.innerHTML= submission_index;
           for (var i = 1; i <= number_of_fields; i++)
           {
               var curr_Cell = new_Row.insertCell(i);
               curr_Cell.innerHTML = curr_submission[i].data;
           }
       }
       ,
       createTableHeaders: function(all_Submissions_Arr, number_of_fields) 
       {
            if(all_Submissions_Arr.length == 0) 
            {
                return false; //No submissions available
            }
            var page = document.getElementById("Submissions_Page");
            var table = document.createElement("table");
            table.setAttribute("id", "Submissions_Table");
            page.appendChild(table);
            var row = table.appendChild(document.createElement("tr")); // The header row of the table

            var first_col = document.createElement("th"); //the first column will count the submissions
            first_col.appendChild(document.createTextNode("#"));
            row.appendChild(first_col);

            //use the first(arbitrary) submission to figure out field labels
            var submission = all_Submissions_Arr[0];
            for (var i = 1; i <= number_of_fields; i++)
            {
                var curr_Header = document.createElement("th");
                curr_Header.appendChild(document.createTextNode(submission[i].field_Label));
                row.appendChild(curr_Header);
            }
            return true; //Table created successfully
       }
    }
    
}
</script>
<style>
h2 {
    color: white;
    font-family: HelveticaNeueW01-75Bold,HelveticaNeueW02-75Bold,HelveticaNeueW10-75Bold,Helvetica Neue,Arial,Helvetica,sans-serif;
    font-weight: 400;
    font-size: 4vw;
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
</style>
