function validate(pw){
  var pw = parseInt(pw);
  var pw_length = pw.length;

  // Defining regular expressions
  var numbers = RegExp("[0-9]");
  var special = RegExp("[^A-Za-z0-9]");

  // matching regular expressions
  console.log(numbers.test(pw));

  var number_found = numbers.test(pw);
  var special_found = special.test(pw);

  // conditionals
  if (pw_length < 5){
    document.getElementById('output').innerHTML = "Please enter a password with at least 5 characters.";
  }
  else if (pw_length > 10){
    document.getElementById('output').innerHTML = "Please enter a password with less than 10 characters.";
  }
  else if (pw > 10){
    document.getElementById('output').innerHTML = "Please enter a password with less than 10 characters.";
  }
  else if (length(number_found) < 0){
    document.getElementById('output').innerHTML = "Your password must contain a number.";
  }
  else if (length(special_found) < 0){
    document.getElementById('output').innerHTML = "Your password must contain a special character.";
  }
  else{
    document.getElementById('output').innerHTML = "Your password was entered correctly.";
  }
}
