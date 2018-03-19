(function ($) {

    /* Background matrix About
         * -------------------------------------------------- */
    var aboutBg = function () {
        var c = document.getElementById("about-canvas");
        var ctx = c.getContext("2d");


        c.height = $("#about-bg").height();
        c.width = $(document).width();

        var chinese = "10";

        chinese = chinese.split("");

        var font_size = 10;
        var columns = c.width / font_size;

        var drops = [];

        for (var x = 0; x < columns; x++)
            drops[x] = 1;

        function draw() {

            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, c.width, c.height);

            ctx.fillStyle = "#730606";
            ctx.font = font_size + "px arial";

            for (var i = 0; i < drops.length; i++) {
                var text = chinese[Math.floor(Math.random() * chinese.length)];
                ctx.fillText(text, i * font_size, drops[i] * font_size);

                if (drops[i] * font_size > c.height && Math.random() > 0.975)
                    drops[i] = 0;

                drops[i]++;
            }
        }

        setInterval(draw, 60);
    };

    /* Background matrix Casting
         * -------------------------------------------------- */
    var castingBg = function () {
        var c = document.getElementById("casting-canvas");
        var ctx = c.getContext("2d");


        c.height = $("#casting-bg").height();
        c.width = $(document).width();

        var chinese = "10";

        chinese = chinese.split("");

        var font_size = 10;
        var columns = c.width / font_size;

        var drops = [];

        for (var x = 0; x < columns; x++)
            drops[x] = 1;

        function draw() {

            ctx.fillStyle = "rgba(0, 0, 0, 0.15)";
            ctx.fillRect(0, 0, c.width, c.height);

            ctx.fillStyle = "#730606";
            ctx.font = font_size + "px arial";

            for (var i = 0; i < drops.length; i++) {
                var text = chinese[Math.floor(Math.random() * chinese.length)];
                ctx.fillText(text, i * font_size, drops[i] * font_size);

                if (drops[i] * font_size > c.height && Math.random() > 0.975)
                    drops[i] = 0;

                drops[i]++;
            }
        }

        setInterval(draw, 60);
    };

    /* Background matrix Subscribe
         * -------------------------------------------------- */
    var subscribeBg = function () {
        var c = document.getElementById("subscribe-canvas");
        var ctx = c.getContext("2d");


        c.height = $("#subscribe-bg").height();
        c.width = $(document).width();

        var chinese = "10";

        chinese = chinese.split("");

        var font_size = 10;
        var columns = c.width / font_size;

        var drops = [];

        for (var x = 0; x < columns; x++)
            drops[x] = 1;

        function draw() {

            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, c.width, c.height);

            ctx.fillStyle = "#730606";
            ctx.font = font_size + "px arial";

            for (var i = 0; i < drops.length; i++) {
                var text = chinese[Math.floor(Math.random() * chinese.length)];
                ctx.fillText(text, i * font_size, drops[i] * font_size);

                if (drops[i] * font_size > c.height && Math.random() > 0.975)
                    drops[i] = 0;

                drops[i]++;
            }
        }

        setInterval(draw, 60);
    };

    /* Initialize
     * ------------------------------------------------------ */
    (function ssInit() {

        aboutBg();
        castingBg();
        subscribeBg();

    })();


})(jQuery);