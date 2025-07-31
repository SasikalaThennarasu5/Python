import React from 'react';
import { FaPhoneAlt, FaEnvelope } from 'react-icons/fa';

const ContactUs = () => {
  return (
    <div className="bg-[#E6E6FA] font-['Poppins'] text-[#1a1a1a] px-6 md:px-24 py-12">
      <h2 className="text-3xl font-semibold text-center mb-6">Contact Us</h2>

      <p className="text-center mb-10 max-w-3xl mx-auto text-base">
        We'd love to hear from you! Whether you have a question, need help customizing your invites,
        or just want to chat about your dream wedding stationery — we're here for you.
      </p>

      {/* --- Support Section --- */}
      <div className="mb-10">
        <div className="flex items-center gap-3 mb-4 text-lg font-semibold">
          <FaPhoneAlt className="text-blue-600 text-[22px]" />
          Support
        </div>
        <div className="pl-8 text-sm space-y-1">
          <p><strong>India (toll free):</strong> 969-264-9444</p>
          <p><strong>Only Call + No WhatsApp Number:</strong></p>
          <p className="text-blue-800">sales@wedknotcraftinvitationcards.com</p>
        </div>
      </div>

      {/* --- Proofing Department --- */}
      <div className="mb-10">
        <div className="flex items-center gap-3 mb-4 text-lg font-semibold">
          <FaEnvelope className="text-purple-600 text-[22px]" />
          Proofing Department
        </div>
        <div className="pl-8 text-sm space-y-3">
          <p><strong>Indian Standard Time (IST)</strong></p>
          <p>Mobile (9.00am to 9.00pm IST) Monday to Saturday</p>
          <div>
            <p><strong>HR Team</strong></p>
            <p>+91 8765432100</p>
            <p className="text-blue-800">hrteam@wedknotcraftinvitationcards.com</p>
          </div>
          <div>
            <p><strong>Customer Support Team</strong></p>
            <p>+91 9876543210</p>
            <p className="text-blue-800">customersupport@wedknotcraftinvitationcards.com</p>
          </div>
        </div>
      </div>

      {/* --- General Contact Text --- */}
      <div className="mb-10">
        <h3 className="text-xl font-bold mb-3">Reach Out</h3>
        <p className="text-base">
          Whether you’re looking for inquiries, would like to ask before ordering, or just want to let us know how we did.
        </p>
      </div>

      {/* --- Description Box (Dropdown-like effect for last info block) --- */}
     
        <h4 className="text-center text-lg font-semibold mb-3">
          An online Invitation Store with Worldwide Delivery
        </h4>
        <p className="mb-2">
          Weddings are always special but the fact about <strong>Wedknotcraft</strong> wedding Cards is that they are bespoke and exquisite in design that win the hearts of millions across the world.
        </p>
        <p className="mb-2">
          The team behind us is extremely talented and has more than 50 years of experience with them to translate your dream wedding card into reality.
        </p>
        <p className="mb-2">
          If you want your wedding card to be truly rare and exceptional then look no further. The team here is fully able to weave dreams into reality.
        </p>
        <p className="mb-4">
          No matter what kind of wedding you have planned, <span className="text-blue-700 underline cursor-pointer">wedknotcraft.in</span> is well known to design various wedding invitations like Hindu Wedding Cards, Muslim Wedding Cards, Sikh Wedding Cards, Interface Wedding Cards and so on.
        </p>
        <p className="text-center font-medium">
          If you have any query related to Invitation designs or our cards, please feel free to contact us!
        </p>

        {/* Decorative left arrow for dropdown look on desktop */}
        <div className="hidden lg:block absolute left-[-12px] top-6 w-0 h-0 border-t-[10px] border-b-[10px] border-r-[12px] border-t-transparent border-b-transparent border-r-white"></div>
      </div>
    
  );
};

export default ContactUs;
