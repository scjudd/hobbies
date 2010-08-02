$imgs = $("#photo_stack img");
$imgCount = $imgs.length;
$curr_index = 0;
$imgs.last().addClass('current'); /* Set the image at top of stack to current */

$("#photo_stack")
    .delegate('img', 'click', function() {
        $this = $(this);

        /* If the image is at the top of the stack */
        if ($this.hasClass('current')) {
            /* Work out new z-index value */
            $zi = $this.css('zIndex') - $imgCount;

            /* Trigger animation */
            $this.addClass('animate');

            /* Assign new z-index value then stop animation after complete */
            setTimeout(function() { $this.css('zIndex', $zi); }, 200);
            setTimeout(function() { $this.removeClass('animate'); }, 1000);

            /* Set next image to current */
            $this.removeClass('current');
            if ($this.index() == 0) {
                $imgs.last().addClass('current');
            } else {
                $imgs.eq($this.index()-1).addClass('current');
            }
        }
    })