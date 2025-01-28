$("#generateBtn").on("click", function(event) {
    var prompt = $("#prompt").val().trim();  
    if (prompt === "") {
        alert("Please enter a prompt before generating an image.");
        return;  
    }
    $("#output-container").css("display", "none"); 
    $("#loading").css("display", "block");
    $.ajax({
        url: "/generate_img",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ "prompt": prompt }),
        success: function(response) {
            if (response.image_url) {
                $("#generated-image").attr("src", response.image_url);
                $("#view-link").attr("href", response.image_url);
                $("#loading").css("display", "none");
                $("#output-container").css("display", "block");
            } else {
                alert("Error generating image");
                $("#loading").css("display", "none");
            }
        },
        error: function() {
            alert("Error generating image");
            $("#loading").css("display", "none");
        }
    });
});