<template>
  <html id="Form_Builder_Page">
    <h2>Build Your Form</h2>
    Form Name: <input type="text" id="Form_Name" class="Inputs">
    <br>
    Field label: <input type="text" id="fieldLabel1" class="Inputs">
    Input name:  <input type="text" id="inputName1" class="Inputs">
    Input type: 
    <select name="input type" id = "inputTypeComboBox1" class="Options">
      <option value="text">  Text  </option>
      <option value="color"> Color </option>
      <option value="date">  Date  </option>
      <option value="email"> Email </option>
      <option value="tel">   Telephone   </option>
      <option value="number">Number</option>
    </select>
    <br>
    <button id="AddFieldButton" class="Buttons" v-on:click="add_Field">Add Field</button>
    <button id="SubmitButton" class="Buttons" v-on:click="add_Form_To_Form_List">Submit</button>
  </html>
</template>


<script>
import Vue from "vue";


export default 
{
    name: 'Form_Builder',  
    data() {
        return {
          fields_Count: 1
        }
    },
    methods: {
      add_Field: function (event) 
      {
        this.fields_Count++; //advance the row counter        
        this.new_Line(); //add new line
        this.new_Line_Field_Label(); //add field label textbox to the new line
        this.new_Line_Input_Name(); //add input name textbox to the new line
        this.new_Line_Input_Type(); //add input type combobox to the new line
        
      }
      ,
      new_Line: function() 
      {
        var Form_Builder_Page = document.getElementById("Form_Builder_Page");
        var add_Field_Button = document.getElementById("AddFieldButton");
        var newLine = document.createElement("br");
        Form_Builder_Page.insertBefore(newLine, add_Field_Button);
      }
      ,
      new_Line_Field_Label: function() 
      {
        var Form_Builder_Page = document.getElementById("Form_Builder_Page");
        var add_Field_Button = document.getElementById("AddFieldButton");
        var new_Field_Label = document.createElement("input");
        new_Field_Label.setAttribute("type", "text");
        new_Field_Label.setAttribute("id", "fieldLabel" + this.fields_Count.toString());
        new_Field_Label.setAttribute("class", "Inputs");
        Form_Builder_Page.insertBefore(document.createTextNode("Field label: "), add_Field_Button);
        Form_Builder_Page.insertBefore(new_Field_Label, add_Field_Button);
      }
      ,
      new_Line_Input_Type: function()
      {
        var Form_Builder_Page = document.getElementById("Form_Builder_Page");
        var add_Field_Button = document.getElementById("AddFieldButton");
        var input_Type_ComboBox = document.getElementById("inputTypeComboBox1");
        var new_Input_Type_ComboBox = input_Type_ComboBox.cloneNode(true);
        new_Input_Type_ComboBox.setAttribute("id", "inputTypeComboBox" + this.fields_Count.toString());
        new_Input_Type_ComboBox.setAttribute("class", "Input_Types");
        Form_Builder_Page.insertBefore(document.createTextNode(" Input type: "), add_Field_Button);
        Form_Builder_Page.insertBefore(new_Input_Type_ComboBox, add_Field_Button);
        Form_Builder_Page.insertBefore(document.createElement("br"), add_Field_Button); //reached end of line
      }
      ,
      new_Line_Input_Name: function() 
      {
        var Form_Builder_Page = document.getElementById("Form_Builder_Page");
        var add_Field_Button = document.getElementById("AddFieldButton");
        var new_Input_Name = document.createElement("input");
        new_Input_Name.setAttribute("type", "text");
        new_Input_Name.setAttribute("id", "inputName" + this.fields_Count.toString());
        new_Input_Name.setAttribute("class", "Inputs");
        Form_Builder_Page.insertBefore(document.createTextNode(" Input name: "), add_Field_Button);
        Form_Builder_Page.insertBefore(new_Input_Name, add_Field_Button);
      }
      ,
      add_Form_To_Form_List: function(event)
      {
        var is_Input_Valid = this.check_Data_Validity();
        
        if(is_Input_Valid)
        {
          //Create a new form in the database:
          var form_Name = {formName: document.getElementById("Form_Name").value} ;
          var jsoned_Form_Name = JSON.stringify(form_Name);
          this.$http.post('http://localhost:5000/add_New_Form', jsoned_Form_Name, {
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Access-Control-Allow-Origin': 'http://localhost:8080'
            }
            }).then( response => {
                //add the fields to the form in the database
                this.add_Fields_To_Form(response.data.toString())
              })
        }
        else
        {
            //ELSE_DO_NOTHING
        }

      }
      ,
      form_Successfully_Added: function()
      {
        setTimeout(function () {
            window.alert("The form was successfully added to the list of forms!");
            window.location = '/';
        }, 200); //Wait some time for the fields to be added to the database
      }
      ,
      add_Fields_To_Form: function(form_Id) 
      {
        var i;
        var all_Fields = [];
        for (i = 1; i <= this.fields_Count; i++)
        {
          var field = { 
                fieldLabel: document.getElementById("fieldLabel" + i.toString()).value,
                inputName : document.getElementById("inputName"  + i.toString()).value,
                inputType : document.getElementById("inputTypeComboBox" + i.toString()).value,
                form_Id   : form_Id,
                index     : i   //this is so that the fields will appear in the same order in "Submit Page"
          };
          all_Fields.push({"fieldLabel": field.fieldLabel,
                            "inputName": field.inputName,
                            "inputType": field.inputType,
                            "form_Id":   field.form_Id,
                            "index":     field.index      });
        }
        var jsoned_fields = JSON.stringify(all_Fields);
        console.log(jsoned_fields);
        
        this.$http.post('http://localhost:5000/add_New_Fields', jsoned_fields, {
           headers: {
             'Accept': 'application/json',
             'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
             'Access-Control-Allow-Origin': 'http://localhost:8080'
           }
        }).then( response => {
                this.form_Successfully_Added()
           })
      }
      ,
      check_Data_Validity: function()
      {
        var i;
        var found_Blanks = false, duplicate_Input_Names = false;
        var Input_Names_Arr = []
        var Form_Name = document.getElementById("Form_Name").value;
        if(Form_Name = '') 
        {
          window.alert("Form name cannot be empty");
          found_Blanks = true;
        }
        for (i = 1; i <= this.fields_Count; i++) 
        { 
          var ith_Field_Label = document.getElementById("fieldLabel" + i.toString()).value;
          var ith_Input_Name  = document.getElementById("inputName"  + i.toString()).value;
          if(ith_Field_Label == '' || ith_Input_Name == '') 
          {
            found_Blanks = true;
            //TODO: red color the blanks here
          }
          if(Input_Names_Arr.includes(ith_Input_Name))
          {
            duplicate_Input_Names = true;
            //TODO: red color duplicate input names
          }
          Input_Names_Arr.push(ith_Input_Name)
        }
        if(found_Blanks == true)
        {
            window.alert("Please fill out all the fields before submitting the form.");
            return false;
        }
        if(duplicate_Input_Names == true)
        {
            window.alert("Input names have to be unique.");
            return false;
        }
        return true;
      }
    }
}




</script>

<style>
html {
  color: white;
  font-family: HelveticaNeueW01-75Bold,HelveticaNeueW02-75Bold,HelveticaNeueW10-75Bold,Helvetica Neue,Arial,Helvetica,sans-serif;
  font-weight: 200;
  font-size: 18px;
}
#Form-Builder {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
h2 {
    color: white;
    font-family: HelveticaNeueW01-75Bold,HelveticaNeueW02-75Bold,HelveticaNeueW10-75Bold,Helvetica Neue,Arial,Helvetica,sans-serif;
    font-weight: 400;
    font-size: 4vw;
    line-height: 1.3;
    margin: 0 0 4%;
}
.Inputs {
  border-width: 0 0 1px;
  border-style: solid;
  background-color: #57c2da;
  text-align: center;
  width: 10%;
  margin-bottom: 20px;
}
.Buttons {
	-moz-box-shadow:inset 0px 1px 0px 0px #54a3f7;
	-webkit-box-shadow:inset 0px 1px 0px 0px #54a3f7;
	box-shadow:inset 0px 1px 0px 0px #54a3f7;
	background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #007dc1), color-stop(1, #0061a7));
	background:-moz-linear-gradient(top, #007dc1 5%, #0061a7 100%);
	background:-webkit-linear-gradient(top, #007dc1 5%, #0061a7 100%);
	background:-o-linear-gradient(top, #007dc1 5%, #0061a7 100%);
	background:-ms-linear-gradient(top, #007dc1 5%, #0061a7 100%);
	background:linear-gradient(to bottom, #007dc1 5%, #0061a7 100%);
	filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#007dc1', endColorstr='#0061a7',GradientType=0);
	background-color:#007dc1;
	-moz-border-radius:3px;
	-webkit-border-radius:3px;
	border-radius:3px;
	border:1px solid #124d77;
	display:inline-block;
	cursor:pointer;
	color:#ffffff;
	font-family:Arial;
	font-size:13px;
	padding:6px 24px;
	text-decoration:none;
	text-shadow:0px 1px 0px #154682;
}
.Buttons:hover {
	background:-webkit-gradient(linear, left top, left bottom, color-stop(0.05, #0061a7), color-stop(1, #007dc1));
	background:-moz-linear-gradient(top, #0061a7 5%, #007dc1 100%);
	background:-webkit-linear-gradient(top, #0061a7 5%, #007dc1 100%);
	background:-o-linear-gradient(top, #0061a7 5%, #007dc1 100%);
	background:-ms-linear-gradient(top, #0061a7 5%, #007dc1 100%);
	background:linear-gradient(to bottom, #0061a7 5%, #007dc1 100%);
	filter:progid:DXImageTransform.Microsoft.gradient(startColorstr='#0061a7', endColorstr='#007dc1',GradientType=0);
	background-color:#0061a7;
}
.Buttons:active {
	position:relative;
	top:1px;
}
#Form_Name {
  margin-bottom: 25px;
  font-family: Georgia, serif;
  font-size: 25px;
  letter-spacing: 2px;
  word-spacing: 2px;
  color: #000000;
  font-weight: 700;
  text-decoration: none;
  font-style: normal;
  font-variant: normal;
  text-transform: none;
  text-align: center;
}

select {
    padding: 5px 8px;
    width: 10%;
    border-width: 0 1px 0 1px;
    border-style: solid;
    box-shadow: none;
    background: #f2f2f2;
    font-family: HelveticaNeueW01-75Bold,HelveticaNeueW02-75Bold,HelveticaNeueW10-75Bold,Helvetica Neue,Arial,Helvetica,sans-serif;
}
</style>
