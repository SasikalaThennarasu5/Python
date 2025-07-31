import React from 'react';
import wedding from '../assets/images/wedding.png';
import prewedding from '../assets/images/prewedding.png';
import tajmahal from '../assets/images/tajmahal.png';

const AboutUs = () => {
  return (
    <div className="bg-primary font-poppins py-10 px-6 md:px-[24px] text-gray-800">
      <h2 className="text-[32px] font-semibold text-center underline mb-12">ABOUT US</h2>

      {/* Section 1 */}
      <div className="grid grid-cols-1 md:grid-cols-12 items-center gap-10 mb-16">
        <div className="md:col-span-6">
          <h3 className="text-[24px] font-semibold mb-2">Celebrating Love, One Invitation at a Time</h3>
          <p className="text-[20px] leading-relaxed">
            At Wed Knot Craft, we believe that every love story is unique and deserves to be celebrated
            in a way that reflects its individuality.
          </p>
        </div>
        <div className="md:col-span-6 flex justify-center">
          <img
            src= {wedding}
            alt="Wedding"
            className="w-60 h-auto rounded-md shadow-md"
          />
        </div>
      </div>

      {/* Section 2 */}
      <div className="grid grid-cols-1 md:grid-cols-12 items-center gap-10 mb-16">
        <div className="md:col-span-6 flex justify-center">
          <img
            src={prewedding}
            alt="Pre-Wedding"
            className="w-60 h-auto rounded-md shadow-md"
          />
        </div>
        <div className="md:col-span-6">
          <h3 className="text-[24px] font-semibold mb-2">OUR STORY</h3>
          <p className="text-[20px] leading-relaxed">
            What started as a passion for design has blossomed into a full-fledged business dedicated
            to bringing couples' visions to life. Our founder, <strong>[Founder's Name]</strong>, envisioned a platform
            where couples could find invitations that resonated with their personal style and cultural heritage.
          </p>
        </div>
      </div>

      {/* Section 3 */}
      <div className="grid grid-cols-1 md:grid-cols-12 items-center gap-10 mb-16">
        <div className="md:col-span-6">
          <h3 className="text-[24px] font-semibold mb-4">OUR PROMISE</h3>
          <ul className="text-[20px] list-disc pl-6 space-y-3 leading-relaxed">
            <li>
              <strong>Custom Designs:</strong> Tailored invitations that reflect your unique love story.
            </li>
            <li>
              <strong>Quality Craftsmanship:</strong> Invitations crafted with attention to detail and high-quality materials.
            </li>
            <li>
              <strong>Customer Satisfaction:</strong> A seamless experience from selection to delivery, ensuring your complete satisfaction.
            </li>
          </ul>
        </div>
        <div className="md:col-span-6 flex justify-center">
          <img
            src={tajmahal}
            alt="Taj Mahal"
            className="w-60 h-auto rounded-md shadow-md"
          />
        </div>
      </div>

      {/* Final CTA */}
      <div className="text-center mt-16">
        <h3 className="text-[24px] font-semibold mb-2 text-amber">JOIN US in Celebrating Your Special Day</h3>
        <p className="text-[20px] max-w-3xl mx-auto">
          Explore our diverse range of designs and let us help you set the tone for your wedding celebration.
          At <strong>[Your Company Name]</strong>, your love story is our inspiration.
        </p>
      </div>
    </div>
  );
};

export default AboutUs;
