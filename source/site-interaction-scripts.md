# zluri.com interaction scripts — extracts

Inline page scripts captured on 11 Nov 2026 that implement the behaviours described in `guidelines/08-web-interactions.md`. Kept as evidence for the timings and easings quoted there. Third-party library code is not included.

## Home — nav dropdown (hover open/close)

```js
function navDropdownAnimation() {
  const dropdowns = document.querySelectorAll("[nav-dropdown]");
  const isTouchDevice = window.matchMedia("(pointer: coarse)").matches;

  dropdowns.forEach(dropdown => {
    const toggle = dropdown.querySelector("[nav-dropdown-toggle]");
    const list = dropdown.querySelector("[nav-dropdown-list]");
    const bg = dropdown.querySelector("[nav-dropdown-bg]");
    const container = dropdown.querySelector("[nav-dropdown-container]");

    let isOpen = false;

    // Initial state
    if (window.innerWidth > 991) {
      gsap.set(list, { pointerEvents: "none" }); // Desktop: use pointer events
    }

    gsap.set(bg, { height: "0%" });
    if (container) gsap.set(container, { opacity: 0 });

    const openDropdown = () => {
      if (isOpen) return;
      isOpen = true;

      toggle.classList.add("is-active");
      gsap.killTweensOf([bg, container]);

      if (window.innerWidth > 991) {
        // Desktop
        gsap.set(list, { pointerEvents: "auto" });
      } else {
        // ✅ Mobile: activate container permanently
        if (container && !container.classList.contains("is-active")) {
          container.classList.add("is-active");
          gsap.set(container, { opacity: 1 });
        }
      }

      gsap.to(bg, {
        height: "calc(100% + 6rem)",
        duration: 0.1,
        ease: "power2.out",
        onComplete: () => {
          if (window.innerWidth > 991 && container) {
            // Desktop animation (unchanged)
            gsap.to(container, {
              opacity: 1,
              duration: 0.1,
              ease: "power2.out",
              onComplete: () => {
                container.classList.add("is-active");
              }
            });
          }
        }
      });
    };

    const closeDropdown = () => {
      if (!isOpen) return;
      isOpen = false;

      toggle.classList.remove("is-active");
      gsap.killTweensOf([bg, container]);

      if (window.innerWidth > 991) {
        // Desktop fade out
        if (container) {
          gsap.to(container, {
            opacity: 0,
            duration: 0.06,
            ease: "power2.out",
            onComplete: () => {
              container.classList.remove("is-active");
            }
          });
        }
      }

      gsap.to(bg, {
        height: "0%",
        duration: 0.06,
        ease: "power2.out",
        onComplete: () => {
          if (window.innerWidth > 991) {
            gsap.set(list, { pointerEvents: "none" });
          }
        }
      });
    };

    if (isTouchDevice) {
      toggle.addEventListener("c
```

## Home — problem slider (Swiper)

```js
/* --- For Swiper Sliders ---*/
$(".home_problem_wrapper").each(function (index) {
  const swiper = new Swiper($(this).find(".swiper")[0], {
    speed: 480,
    autoHeight: false,
    followFinger: true,
    freeMode: false,
    slideToClickedSlide: false,
    slidesPerView: 3,
    spaceBetween: 20,
    rewind: false,
    mousewheel: {
      forceToAxis: true
    },
    keyboard: {
      enabled: true,
      onlyInViewport: true
    },
    breakpoints: {
      // mobile landscape
      280: {
        slidesPerView: 1.1,
        
      },
      // tablet
      768: {
        slidesPerView: 2,
         },
      // desktop
      992: {
        slidesPerView: 3,
      }
    },
    navigation: {
      nextEl: $(this).find(".swiper-next")[0],
      prevEl: $(this).find(".swiper-prev")[0],
      disabledClass: "is-disabled"
    },
    
    slideActiveClass: "is-active",
    slideDuplicateActiveClass: "is-active"
  });
});
```

## Home — IRIS layer stack (hover)

```js
document.addEventListener("DOMContentLoaded", () => {

    const links = document.querySelectorAll(".home_foundation_link")
    const paras = document.querySelectorAll(".home_foundation_content")
    const groups = document.querySelectorAll(".home_foundation_media")

    function activate(i) {

      links.forEach(l => l.classList.remove("is_active"))
      links[i].classList.add("is_active")

      paras.forEach(p => p.classList.remove("is_active"))
      paras[i].classList.add("is_active")

      const textItems = paras[i].querySelectorAll(".home_foundation_content_para")
      gsap.fromTo(textItems,
                  { y: 20, opacity: 0 },
                  {
        y: 0,
        opacity: 1,
        duration: 0.6,
        stagger: 0.12,
        ease: "power2.out"
      }
                 )


      groups.forEach((group, index) => {

        const transparent = group.querySelector(".home_foundation_layer_transparent")
        const inactive = group.querySelector(".home_foundation_layer_inactive")
        const active = group.querySelector(".home_foundation_layer_active")

        let y = 0

        /* IMAGE LAYER LOGIC (unchanged) */

        if (index < i) {

          gsap.to(transparent, { opacity: 1, duration: .35 })
          gsap.to(inactive, { opacity: 0, duration: .35 })
          gsap.to(active, { opacity: 0, duration: .35 })

        }

        else if (index === i) {

          gsap.to(active, { opacity: 1, duration: .35 })
          gsap.to(transparent, { opacity: 0, duration: .35 })
          gsap.to(inactive, { opacity: 0, duration: .35 })

        }

        else {

          gsap.to(inactive, { opacity: 1, duration: .35 })
          gsap.to(transparent, { opacity: 0, duration: .35 })
          gsap.to(active, { opacity: 0, duration: .35 })

        }

        /* MOVEMENT LOGIC */

        if (i === 0) {

          y = 0

        }

        else if (i === 1) {

          if (index < 1) y = -40
          if (index > 1) y = 40

        }

        else if (i === 2) {

          if (index < 2) y = -40
          if (index === 3) y = 40

        }

        else if (i === 3) {

          if (index < 3) y = -40

        }

        gsap.to(group, {
          y: y,
          duration: 0.6,
          ease: "power2.out"
        })

      })

    }

    /* hover events */

    links.forEach((link, i) => {
      link.addEventListener("mouseenter", () => activate(i))
    })
    groups.forEach((group, i) => {
      group.addEventListener("mouseenter", () => activate(i))
    })

    /* page load initial state */

    activate(0)

  })
```

## Home — stacked capability cards (scroll blur/scale)

```js
/* --- for product cards blur --- */
if (window.innerWidth > 991) {
  const cards = document.querySelectorAll("[product-card]");

  cards.forEach((card, index) => {
    if (index === 0) return;

    gsap.to(cards[index - 1], {
      scale: 0.99,
      filter: "blur(5px)",
      duration: 0.8,
      ease: "power1.out",
      scrollTrigger: {
        trigger: card,
        start: "top 50%",
        end: "top 20%",
        scrub: 1,
      },
    });
  });
}
```

## Home — hide nav during sticky tabs

```js
// Hide navbar on Tabs section

const hideNavbar = () => {
  ScrollTrigger.create({
    trigger: '.section_home_capabilities',
    start: 'top 0%',
    onToggle: (self) => {
      if (self.isActive) {
        gsap.to('.nav_component_wrap', {
          y: '-110%',
          duration: 1,
          ease: 'power3.out',
          overwrite: true,
        });
      } else {
        gsap.to('.nav_component_wrap', {
          y: '0%',
          duration: 0.5,
          ease: 'power3.out',
          clearProps: 'transform',
          overwrite: true,
        });
      }
    },
  });
};

if(window.innerWidth > 991){
hideNavbar()
}
```

## Home — product tabs switch on hover

```js
document.querySelectorAll('.products_tab_link').forEach(function(el) {
  el.addEventListener('mouseenter', function() {
    el.click();
  });
});
```

## Home — logo marquee (Splide auto-scroll)

```js
new Splide(".splide", {
    type: "loop",
    autoWidth: true,
    height: "auto",
    drag: "free",
    arrows: false,
    pagination: false,
    label: "Image Slider",
    reduceMotion: {
      speed: 0,
      rewindSpeed: 0,
      autoplay: "pause"
    },
    autoScroll: {
      speed: .8
    },
    breakpoints: {
      991: {
        autoScroll: {
          speed: .8
        }
      },
      767: {
        autoScroll: {
          speed: .8
        }
      }
    }
  }).mount(window.splide.Extensions);
```

## UIC — pinned connector scene

```js
document.addEventListener('DOMContentLoaded', function () {
    gsap.registerPlugin(ScrollTrigger);

    let scrollInstance = null;

    function initScroll() {
        // only run above 991px
        if (window.innerWidth > 991) {

            const wrapper = document.querySelector('.uic_connect_wrapper');
            const cards = document.querySelectorAll('.uic_connect_card');
            const lines = document.querySelectorAll('.grid-path');
            const platform = document.querySelector('.uic_connect_bottom_footer');

            const stepPX = 300;
            const totalSteps = cards.length;
            const totalScroll = (totalSteps + 1) * stepPX;

            let lastStep = 1;

            scrollInstance = ScrollTrigger.create({
                trigger: wrapper,
                start: "top top",
                end: `+=${totalScroll}`,
                scrub: true,
                pin: true,

                onUpdate: (self) => {
                    const scrolledPx = self.scroll() - self.start;
                    const currentStep = Math.floor(scrolledPx / stepPX);

                    if (currentStep !== lastStep) {
                        lastStep = currentStep;
                    }

                    cards.forEach((card, i) => {
                        card.classList.toggle('active', i <= currentStep);
                    });

                    lines.forEach((line, i) => {
                        line.classList.toggle('active', i <= currentStep);
                    });

                    if (platform) {
                        platform.classList.toggle('active', currentStep >= totalSteps);
                    }
                }
            });

        }
    }

    function destroyScroll() {
        if (scrollInstance) {
            scrollInstance.kill();
            scrollInstance = null;
        }
    }

    // init on load
    initScroll();

    // handle resize
    window.addEventListener('resize', () => {
        if (window.innerWidth > 991) {
            if (!scrollInstance) initScroll();
        } else {
            destroyScroll();
        }
    });
});
```

## ISPM — isolate on hover

```js
document.addEventListener("DOMContentLoaded", () => {

  if (window.innerWidth < 992) return;

  const section = document.querySelector(".section_ispm_foundation");

  const links = Array.from(section.querySelectorAll(".ispm_foundation_link"));
  const medias = Array.from(section.querySelectorAll(".ispm_foundation_media_group"));

  // 👉 Activate all
  const activateAll = () => {
    links.forEach(el => el.classList.add("is_active"));
    medias.forEach(el => el.classList.add("is_active"));
  };

  // 👉 Activate single pair
  const activateSingle = (index) => {
    links.forEach((el, i) => {
      el.classList.toggle("is_active", i === index);
    });

    medias.forEach((el, i) => {
      el.classList.toggle("is_active", i === index);
    });
  };

  // 👉 Initial state
  activateAll();

  // 👉 Link hover
  links.forEach((link, i) => {
    link.addEventListener("mouseenter", () => activateSingle(i));
    link.addEventListener("mouseleave", activateAll);
  });

  // 👉 Media hover
  medias.forEach((media, i) => {
    media.addEventListener("mouseenter", () => activateSingle(i));
    media.addEventListener("mouseleave", activateAll);
  });

});
```

## State of AI — path draw, sibling dim, highlight wipe

```js
document.addEventListener('DOMContentLoaded', function () {
gsap.set(".page-wrapper", { opacity: 1 });


/*--- for popup ---*/
function popupHandler() {
  const popupWrap = document.querySelector('[popup-wrap]');
  const popupButtons = document.querySelectorAll('[popup-btn]');
  const popupClose = document.querySelector('[popup-close]');

  if (!popupWrap) return;

  popupButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      popupWrap.classList.add('is-active');
    });
  });

  popupClose?.addEventListener('click', () => {
    popupWrap.classList.remove('is-active');
  });
}

popupHandler();


gsap.registerPlugin(ScrollTrigger);

/*--- For SVG Path Animation ---*/
  function svgPathAnimation() {
    const containers = document.querySelectorAll("[svg-container]");

    containers.forEach((container) => {
      const path = container.querySelector("path");
      const progressSpan = container.querySelector("[svg-progress]");

      if (!path) return;

      const pathLength = path.getTotalLength();

      gsap.set(path, {
        strokeDasharray: pathLength,
        strokeDashoffset: pathLength,
      });

      gsap.to(path, {
        strokeDashoffset: 0,
        duration: 1,
        ease: "none",
        scrollTrigger: {
          trigger: container,
          start: "top 40%",
          end: "bottom 40%",
          scrub: 1,
          onUpdate: (self) => {
            if (progressSpan) {
              const progress = Math.round(self.progress * 100);
              progressSpan.textContent = progress + '%';
            }
          },
        }
      });
    });

    // Refresh ScrollTrigger on window resize
    window.addEventListener('resize', () => {
      ScrollTrigger.refresh();
    });
  }

  // Call the function
  if (window.innerWidth > 991) {
  svgPathAnimation();
}




/*--- For AI Leaderboard Section ---*/
  const links = document.querySelectorAll('.ai_lb_block');
  links.forEach(link => {
    link.addEventListener('mouseenter', () => {
      links.forEach(l => {
        if (l !== link) {
          l.style.opacity = '0.6'; 
        }
      });
    });
    link.addEventListener('mouseleave', () => {
      links.forEach(l => {
        l.style.opacity = '1'; 
      });
    });
  });
  



/*--- For Text Highlight ---*/
  document.querySelectorAll("[text-highlight]").forEach((el) => {
    // Wrap content in inner span
    const inner = document.createElement("span");
    inner.className = "text-inner";
    inner.textContent = el.textContent;
    el.textContent = "";
    el.appendChild(inner);

    // Animate background size to reveal highlight only under real text
    gsap.fromTo(inner,
      { backgroundSize: "0% 100%" },
      {
        backgroundSize: "100% 100%",
        duration: 1,
        ease: "power2.out",
        scrollTrigger: {
          trigger: el,
          start: "top 80%",
          toggleActions: "play none none none"
        }
      }
    );
  });
 





  
  
  


/*--- For AI Cat Lead Section ---*/ 
function sectionTabChange() {
    const tablinks = document.querySelectorAll('.ai_cat_lead_link');
    const tabPanes = document.querySelectorAll('.ai_cat_lead_pane');
    const wrap = document.querySelector('.ai_cat_lead_wrap');
    const count = tabPanes.length;
    const isDesktop = window.innerW
```

## Unicorn Studio embeds

- Home hero: `data-us-project="knTE0cKfOKf6YYcCEMMQ"`, `data-us-fps="60"`, `data-us-dpi="1.5"`
- Light-ray band (home CTA, UIC hero): `data-us-project="tGQxeNcMSW4lPskGmzPr"`
- Loader: `unicornstudio.js@v2.1.4`

## Button hover (computed)

`.cta_button` transition: `background-color 0.44s cubic-bezier(0.215, 0.61, 0.355, 1)`; primary hover background `#1d4ba6`.
