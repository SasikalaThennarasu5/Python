import React from 'react';
import heroImage from '../assets/images/hero2.png'; // Update filename if needed

const Hero2 = () => {
  return (
    <section className="bg-[#E6E6FA] py-8 flex justify-center items-center min-h-[60vh] px-4">
      <img
        src={heroImage}
        alt="Hero Section"
        className="w-full max-w-7xl h-auto rounded-xl shadow-md object-cover"
      />
    </section>
  );
};

export default Hero2;
