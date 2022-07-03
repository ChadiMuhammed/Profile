<!DOCTYPE html >
<html lang = "en" >

<head >
<meta charset = "UTF-8" >
<meta http-equiv = "X-UA-Compatible" content = "IE=edge" >
<meta name = "viewport" content = "width=device-width, initial-scale=1.0" >
    <title > {% block title % }{ % endblock % } < /title >
    <link rel = "stylesheet" href = "{{ url_for('static', filename='portfolio.css') }}" >

    <script src = "https://kit.fontawesome.com/be250b723e.js" crossorigin = "anonymous" > </script >
</head >

<body >
    {% blockbody%}

    { % endblock % }
</body >

</html >
