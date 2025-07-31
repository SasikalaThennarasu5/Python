import React from 'react';
import heroImg from '../assets/images/hero3.png'; // Update filename if needed

const hero3 = () => {
  return (
    <section className="w-full h-[40vh] md:h-[50vh] bg-cover bg-center" style={{ backgroundImage: `url(${heroImg})` }}>
              {/* Optional overlay */}
              <div className="w-full h-full bg-black/20 flex items-center justify-center">
                {/* Optional content can go here */}
                {/* <h1 className="text-white text-3xl md:text-5xl font-bold">Welcome</h1> */}
              </div>
            </section>
  );
};

export default hero3;
