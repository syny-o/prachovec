    var page = 1;
    var emptyPage = false;
    var blockRequest = false;

    let btnNext = document.getElementById("btn-next");
    let totalPages = btnNext.getAttribute('data-count');
    let spinner = document.getElementById("spinner");
    let caption = document.getElementById("caption")
    const initialCaptionText = caption.textContent;
    console.log(totalPages)

    btnNext.addEventListener('click', function (e) {
        if (!emptyPage && !blockRequest) {
            blockRequest = true;
            page += 1;
            console.log(page)
            console.log(totalPages)

            spinner.style.display = "inline-block"
            caption.textContent = '';
            fetch('?photos_only=1&page=' + page)
                .then(response => response.text())
                .then(html => {
                    if (html === '') {
                        emptyPage = true;
                    }
                    else {
                        var imageList = document.getElementById('image-list');
                        imageList.insertAdjacentHTML('beforeEnd', html);
                        blockRequest = false;
                        spinner.style.display = "none";
                        caption.textContent = initialCaptionText;
                        if (page == totalPages) {
                            btnNext.style.display = "none";
                        }
                    }
                })

        }

    });

