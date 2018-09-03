<template>
    <html>
        <h2>Form Submission</h2>
        <form id="Submit_Form_Page" v-on:submit.prevent="submit_Form">
            <input id="Submit_Button" type="submit" value="Submit">
        </form>
    </html>
</template>

<script>
import Vue from "vue";


export default 
{
    name: 'Submit_Page',
    data() {
        return {
          form_id: window.location.pathname.slice("/Submit-Page/".length)
        }
    }, 
    created : function () 
    {
        this.get_Form_Data();
    }
    ,
    methods: 
    {
        get_Form_Data: function()
        {
            var all_Fields_Arr = [];
            this.$http.get('http://localhost:5000/get_Form_Fields?form_id=' + this.form_id, "", {
            headers: {
              'Accept': 'text/html',
              'Content-Type': 'text/html',
              'Access-Control-Allow-Origin': 'http://localhost:8080'
            }
            }).then( response => {
                all_Fields_Arr = response.data,
                this.display_All_Fields(all_Fields_Arr)
              })
        }
        ,
        display_All_Fields: function(all_Fields_Arr)
        {
            var idx;
            var inputs = document.getElementById("Submit_Form_Page");
            //add the fields to the form
            for (idx = 1; idx <= all_Fields_Arr.length ; idx++)
            {
                //get the field by index to make sure fields are ordered like they were in the Form Builder
                var curr_Field = this.find_Field_By_Index(all_Fields_Arr, idx);
                //add the field
                this.add_Field(curr_Field.fieldLabel, curr_Field.inputName, curr_Field.inputType, idx);
            }
            
        }
        ,
        add_Field: function(fieldLabel, inputName, inputType, index)
        {
            var inputs = document.getElementById("Submit_Form_Page");
            var Submit_Button = document.getElementById("Submit_Button");
            
            //input textbox
            var textbox = document.createElement("input");
            textbox.setAttribute("placeholder", fieldLabel);
            textbox.setAttribute("id", index.toString()); //needed for the fields to appear in the same order in "Submissions Page"
            textbox.setAttribute("type", inputType);
            textbox.setAttribute("name", inputName);
            textbox.setAttribute("class", "Input_Fields");
            textbox.required = true;
            inputs.insertBefore(textbox, Submit_Button);
            //new line
            inputs.insertBefore(document.createElement("br"), Submit_Button);
        }
        ,
        find_Field_By_Index: function(all_Fields_Arr, index)
        {
            for (var i = 0; i < all_Fields_Arr.length ; i++)
            {
                var curr_Index = all_Fields_Arr[i].index;
                if(curr_Index == index) 
                {
                    return all_Fields_Arr[i];
                }
            }
        }
        ,
        submit_Form: function()
        {
            var input_Fields = document.getElementsByClassName("Input_Fields");
            var all_Fields_Obj = {};
            for(var idx = 1; idx <= input_Fields.length; idx++)
            {
                var curr_Field = document.getElementById(idx.toString());
                var field = { 
                inputName : curr_Field.getAttribute("name"),
                data      : curr_Field.value
                // inputType : document.getElementById("inputTypeComboBox" + i.toString()).value,
                };
                // var jsoned_field = JSON.stringify(field);
                all_Fields_Obj[idx.toString()] = field;
            }
            all_Fields_Obj["form_Id"] = this.form_id.toString();
            var all_Fields_JSON = JSON.stringify(all_Fields_Obj);
            this.$http.post('http://localhost:5000/submit_Form', all_Fields_JSON, {
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Access-Control-Allow-Origin': 'http://localhost:8080'
            }
            }).then( response => {
                this.form_Successfully_Submitted()
              })
        }
        ,
        form_Successfully_Submitted: function()
        {
            setTimeout(function () {
                window.alert("The form was successfully submitted!");
                window.location = '/';
            }, 200); //Wait some time for the fields to be added to the database
        }
    }
    
}
</script>
<style>
html {
    background-color: #57c2da;
}
h2 {
    color: white;
    font-family: HelveticaNeueW01-75Bold,HelveticaNeueW02-75Bold,HelveticaNeueW10-75Bold,Helvetica Neue,Arial,Helvetica,sans-serif;
    font-weight: 400;
    font-size: 4vw;
    line-height: 1.15;
    margin: 0 0 6%;
}
#Submit_Button {
    font-size: 2vw;
    color: #3182c8;
    background-color: #fff;
    font-family: HelveticaNeueW01-65Medi,HelveticaNeueW02-65Medi,HelveticaNeueW10-65Medi,Helvetica Neue,Arial,Helvetica,sans-serif;
    padding: .4em 1.5em;
    border-radius: 1em;
    display: inline-block;
    line-height: 1.6;
    margin: 0 0 5px;
    position: relative;
    margin-bottom: 5px;
    cursor: pointer;
    text-align: center;
    -webkit-font-smoothing: antialiased;
    font-weight: 300;
    margin-top: 30px;
}
#Submit_Button:hover {
    background-color: #62a7e4;
    color: #fff;
    transition: background-color .3s,color .3s ease-in-out;
}


input {
    line-height: 30px;
    border-width: 0 0 1px;
    border-style: solid;
    background-color: white;
    margin-bottom: 10px;
}
p {
    color: white;
}
</style>
