<template>
  <html id="Form_Builder_Page">
    Field label: <input type="text" id="fieldLabel1">
    Input name:  <input type="text" id="inputName1">
    input type: 
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
          row_Count: 1  
        }
    },
    methods: {
      add_Field: function (event) 
      {
        this.row_Count++; //advance the row counter        
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
        new_Field_Label.setAttribute("id", "fieldLabel" + this.row_Count.toString());
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
        new_Input_Type_ComboBox.setAttribute("id", "inputTypeComboBox" + this.row_Count.toString());
        Form_Builder_Page.insertBefore(document.createTextNode("Input type: "), add_Field_Button);
        Form_Builder_Page.insertBefore(new_Input_Type_ComboBox, add_Field_Button);
      }
      ,
      new_Line_Input_Name: function() 
      {
        var Form_Builder_Page = document.getElementById("Form_Builder_Page");
        var add_Field_Button = document.getElementById("AddFieldButton");
        var new_Input_Name = document.createElement("input");
        new_Input_Name.setAttribute("type", "text");
        new_Input_Name.setAttribute("id", "inputName" + this.row_Count.toString());
        Form_Builder_Page.insertBefore(document.createTextNode("Input name: "), add_Field_Button);
        Form_Builder_Page.insertBefore(new_Input_Name, add_Field_Button);
      }
      ,
      add_Form_To_Form_List: function(event)
      {
        var i;
        var found_Blanks = false;
        for (i = 1; i <= this.row_Count; i++) { 
          var ith_Field_Label = document.getElementById("fieldLabel" + i.toString());
          var ith_Input_Name  = document.getElementById("inputName"  + i.toString());

          if(ith_Field_Label.value == '' || ith_Input_Name.value == '') 
          {
            found_Blanks = true;
            //TODO: red color the blanks here
          }
        }
        if(!found_Blanks)
        {
          console.log("All is well");
        }
        else
        {
          console.log("Field label and input name cannot be blank");
        }
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
