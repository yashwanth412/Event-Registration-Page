// JavaScript for rotating poster slideshow
document.addEventListener('DOMContentLoaded', function () {
 const posters = document.querySelectorAll('.poster-container .poster');
 let currentIndex = 0;

 function showNextPoster() {
   posters[currentIndex].style.opacity = '0'; // Hide current poster
   currentIndex = (currentIndex + 1) % posters.length; // Cycle to the next poster
   posters[currentIndex].style.opacity = '1'; // Show next poster
 }

 // Show the first poster initially
 posters[currentIndex].style.opacity = '1';

 // Rotate the posters every 5 seconds
 setInterval(showNextPoster, 5000);
});

document.addEventListener('DOMContentLoaded', function () {
 const photoContainer = document.querySelector('.FooterPhoto');
 let scrollAmount = 1;

 function scrollPhotos() {
   photoContainer.scrollLeft += scrollAmount;
   if (photoContainer.scrollLeft === (photoContainer.scrollWidth - photoContainer.clientWidth) || photoContainer.scrollLeft === 0) {
     scrollAmount = -scrollAmount; // Reverse scrolling direction
   }
 }

 // Start scrolling photos
 const scrollInterval = setInterval(scrollPhotos, 50); // Adjust scroll speed as needed

 // Stop scrolling on mouse hover
 photoContainer.addEventListener('mouseenter', function () {
   clearInterval(scrollInterval);
 });

 // Resume scrolling on mouse leave
 photoContainer.addEventListener('mouseleave', function () {
   scrollInterval = setInterval(scrollPhotos, 50); // Adjust scroll speed as needed
 });
});