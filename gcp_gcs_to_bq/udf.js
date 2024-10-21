function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.id = values[0];
    obj.first_name = values[1];
    obj.last_name = values[2];
    obj.email = values[3];
    obj.age = values[4];
    obj.gender = values[5];
    obj.country = values[6];
    obj.signup_date = values[7];
    obj.last_login = values[8];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }
   