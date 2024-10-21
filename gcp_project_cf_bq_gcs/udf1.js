function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.userId = values[0];
    obj.id = values[1];
    obj.title = values[2];
    obj.body = values[3];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }
   