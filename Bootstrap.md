# Using Bootstrap

## Dropdowns

### Resources

[W3schools dropdown](https://www.w3schools.com/bootstrap/bootstrap_dropdowns.asp#:~:text=To%20open%20the%20dropdown%20menu,the%20button%20is%20a%20dropdown.)

[bootstrap dropdowns](https://getbootstrap.com/docs/4.1/components/dropdowns/)

### classes 
bootstap used the classes: 
`dropdown-menu` for creating a menu 
`dropdown-item-text` for creating a non interactive menu
`dropdown-item`
`dropdown-header` to give the dropdown menu a title
`disabled` to gray out an option
`active` to enphasize an option
`dropdown-menu-right` to change the location
`dropdown`
`dropup`
`dropdown-divider` to add a devider to the menu

### Example

```
<div class="container">
  <h2>Dropdowns</h2>
  <p>The .dropdown-header class is used to add headers inside the dropdown menu:</p>
  <div class="dropdown">
    <button class="btn btn-default dropdown-toggle" type="button" data-toggle="dropdown">Tutorials
    <span class="caret"></span></button>
    <ul class="dropdown-menu">
      <li class="dropdown-header">Dropdown header 1</li>
      <li><a href="#">HTML</a></li>
      <li><a href="#">CSS</a></li>
      <li><a href="#">JavaScript</a></li>
      <li class="divider"></li>
      <li class="dropdown-header">Dropdown header 2</li>
      <li><a href="#">About Us</a></li>
    </ul>
  </div>
</div>
```

## Select 

### Resources

[Bootstrap Select](https://getbootstrap.com/docs/5.0/forms/select/)

### Classes
bootstap used the classes:
`form-select`

### HTML

`<select arial-label="Default">`
`<option value='value'>Label</option>`

### Scripting
```
$('#empid').on('click',function() {
  alert($(this).val());
  console.log($(this).val());
});
```
