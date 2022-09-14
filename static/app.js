

const box = document.querySelector('.box')

//function borrowed and modified from codepen: https://codepen.io/GreenSock/pen/mdqXLZL
setTimeout(function () {
// gsap.registerPlugin(ScrollTrigger);

let limit = {max: 100, pullRatio: 0},
    getRandom = () => gsap.utils.random(-limit.max, limit.max),
    round = value => Math.round(value * 5000) / 5000,
    getModifier = home => value => {
      value = parseFloat(value);
      return round(value + (home - value) * limit.pullRatio) + "px";
    };

gsap.utils.toArray(".boxleft").forEach((element) => {
  wander(element, gsap.getProperty(element, "x"), gsap.getProperty(element, "y"))
});

function wander(element, homeX, homeY) {
  gsap.set(element, {
    x: homeX + (gsap.getProperty(element, "x") - homeX) / (1 - limit.pullRatio),
    y: homeY + (gsap.getProperty(element, "y") - homeY) / (1 - limit.pullRatio)
  })
  gsap.to(element, {
    x: homeX + getRandom(),
    y: homeY + getRandom(),
    modifiers: {
      x: getModifier(homeX),
      y: getModifier(homeY)
    },
    duration: gsap.utils.random(1, 4), 
    ease: "tan.inOut",
    onComplete: () => wander(element, homeX, homeY)
  });
}
}, 100)

setTimeout(function () {
  // gsap.registerPlugin(ScrollTrigger);

let limit = {max: 100, pullRatio: 0},
    getRandom = () => gsap.utils.random(-limit.max, limit.max),
    round = value => Math.round(value * 5000) / 5000,
    getModifier = home => value => {
      value = parseFloat(value);
      return round(value + (home - value) * limit.pullRatio) + "px";
    };

gsap.utils.toArray(".boxright").forEach((element) => {
  wander(element, gsap.getProperty(element, "x"), gsap.getProperty(element, "y"))
});

function wander(element, homeX, homeY) {
  gsap.set(element, {
    x: homeX + (gsap.getProperty(element, "x") - homeX) / (1 - limit.pullRatio),
    y: homeY + (gsap.getProperty(element, "y") - homeY) / (1 - limit.pullRatio)
  })
  gsap.to(element, {
    x: homeX + getRandom(),
    y: homeY + getRandom(),
    modifiers: {
      x: getModifier(homeX),
      y: getModifier(homeY)
    },
    duration: gsap.utils.random(1, 3), 
    ease: "tan.inOut",
    onComplete: () => wander(element, homeX, homeY)
  });
}
}, 100)


setTimeout(function () {
  $('.item-info-select').change(function() {
    if ($(this).val() == 0) {
      $('.item-info-price-canvas').css('display', 'none')
      $('.item-info-price-poster').css('display', 'flex')
      $('.item-info-price-digital').css('display', 'none')
    }
    if ($(this).val() == 1) {
      $('.item-info-price-canvas').css('display', 'flex')
      $('.item-info-price-poster').css('display', 'none')
      $('.item-info-price-digital').css('display', 'none')
    }
    if ($(this).val() == 2) {
      $('.item-info-price-canvas').css('display', 'none')
      $('.item-info-price-poster').css('display', 'none')
      $('.item-info-price-digital').css('display', 'flex')
    }
  });

}, 500)
