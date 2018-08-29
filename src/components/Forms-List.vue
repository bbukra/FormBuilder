<template>
    <html>
        <body>
            <p> in forms list page!!! </p>
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

<script src="./Forms-List.js"></script>
<style src="./Forms-List.css"></style>
