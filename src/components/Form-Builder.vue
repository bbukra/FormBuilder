<template>
  <html id="Form_Builder_Page">
    Form Name: <input type="text" id="Form_Name">
    <br>
    Field label: <input type="text" id="fieldLabel1">
    Input name:  <input type="text" id="inputName1">
    Input type: 
    <select name="input type" id = "inputTypeComboBox1">
      <option value="text">  text  </option>
      <option value="color"> color </option>
      <option value="date">  date  </option>
      <option value="email"> email </option>
      <option value="tel">   tel   </option>
      <option value="number">number</option>
    </select>

    <button id="AddFieldButton" v-on:click="add_Field">Add Field</button>
    <br>
    <button id="SubmitButton" v-on:click="add_Form_To_Form_List">Submit</button>
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
        Form_Builder_Page.insertBefore(document.createTextNode(" Input type: "), add_Field_Button);
        Form_Builder_Page.insertBefore(new_Input_Type_ComboBox, add_Field_Button);
      }
      ,
      new_Line_Input_Name: function() 
      {
        var Form_Builder_Page = document.getElementById("Form_Builder_Page");
        var add_Field_Button = document.getElementById("AddFieldButton");
        var new_Input_Name = document.createElement("input");
        new_Input_Name.setAttribute("type", "text");
        new_Input_Name.setAttribute("id", "inputName" + this.fields_Count.toString());
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
                this.add_Fields_To_Form(response.data.toString()),
                this.form_Successfully_Added()
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
        for (i = 1; i <= this.fields_Count; i++)
        {
          var field = { 
                fieldLabel: document.getElementById("fieldLabel" + i.toString()).value,
                inputName : document.getElementById("inputName"  + i.toString()).value,
                inputType : document.getElementById("inputTypeComboBox" + i.toString()).value,
                form_Id   : form_Id,
                index     : i   //this is so that the fields will appear in the same order in "Submit Page"
          };
          var jsoned_field = JSON.stringify(field);
          this.$http.post('http://localhost:5000/add_New_Field', jsoned_field, {
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
              'Access-Control-Allow-Origin': 'http://localhost:8080'
            }
          })
        }
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

// })
<style>
#Form-Builder {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
