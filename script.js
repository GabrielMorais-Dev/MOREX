const tl = gsap.timeline({
  scrollTrigger:{
    trigger:".hero",
    start:"top top",
    end:"+=2500",
    scrub:1.5,
    pin:true
  }
})

tl.to(".img",{
  opacity:0,
  duration:.2
})

.to([".bottle",".cap",".rolha"],{
  opacity:1,
  duration:.2
},"<")