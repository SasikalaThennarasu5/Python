import React from "react";
import { Link } from "react-router-dom";
import {
  FaInstagram,
  FaFacebook,
  FaYoutube,
  FaWhatsapp,
  FaPhoneAlt,
  FaEnvelope,
  FaRegCopyright,
} from "react-icons/fa";
import logo from "../assets/images/footerlogo.png";

const Footer = () => {
  return (
    <footer className="bg-[#FFE5B4] text-black px-4 sm:px-6 md:px-12 lg:px-20 pt-8 pb-4 text-sm sm:text-base md:text-[16px] lg:text-[18px]">
      {/* Top Section */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
        {/* Logo + Description */}
        <div className="flex flex-col items-center lg:items-start text-center lg:text-left">
          <div className="relative">
            <img src={logo} alt="Logo" className="w-[200px] h-[160px] mb-4" />
          </div>
          <p className="font-bold mb-4 text-base sm:text-[17px] md:text-[18px] text-center">
            Largest Wedding <br /> Cards Collections in <br /> Chennai
          </p>
          <div className="flex items-center space-x-4 mt-2">
            <p className="font-bold mb-0 text-sm sm:text-base">
              Follow us with
            </p>
            <div className="flex space-x-3 text-[20px] sm:text-[22px] md:text-[24px]">
              <a
                href="https://www.instagram.com/"
                target="_blank"
                rel="noopener noreferrer"
              >
                <FaInstagram className="text-pink-600 hover:scale-110 transition-transform" />
              </a>
              <a
                href="https://www.facebook.com/"
                target="_blank"
                rel="noopener noreferrer"
              >
                <FaFacebook className="text-blue-600 hover:scale-110 transition-transform" />
              </a>
              <a
                href="https://www.youtube.com/"
                target="_blank"
                rel="noopener noreferrer"
              >
                <FaYoutube className="text-red-600 hover:scale-110 transition-transform" />
              </a>
              <a
                href="https://wa.me/919876543210"
                target="_blank"
                rel="noopener noreferrer"
              >
                <FaWhatsapp className="text-green-600 hover:scale-110 transition-transform" />
              </a>
            </div>
          </div>
        </div>

        {/* Information Links */}
        <div>
          <h3 className="font-bold text-lg sm:text-xl mb-4">Information</h3>
          <ul className="space-y-2">
            <li>
              <Link to="/aboutUs" className="hover:underline font-semibold">
                About Us
              </Link>
            </li>
            <li>
              <Link to="/contactUs" className="hover:underline font-semibold">
                Contact Us
              </Link>
            </li>
            <li>
              <Link to="/FAQ" className="hover:underline font-semibold">
                FAQ
              </Link>
            </li>
            <li>
              <Link to="/howToOrder" className="hover:underline font-semibold">
                How to order wedding invitation online?
              </Link>
            </li>
          </ul>
        </div>

        {/* Quick Access */}
        <div>
          <h3 className="font-bold text-lg sm:text-xl mb-4">Quick Access</h3>
          <ul className="space-y-2">
            <li>
              <Link to="/" className="hover:underline font-semibold">
                Home
              </Link>
            </li>
            <li>
              <Link to="/wedding-cards" className="hover:underline font-semibold">
                Wedding Cards
              </Link>
            </li>
            <li>
              <Link to="/hindu-wedding-cards" className="hover:underline font-semibold">
                Hindu Wedding Cards
              </Link>
            </li>
          </ul>
        </div>

        {/* Contact Us */}
        <div>
          <h3 className="font-bold text-lg sm:text-xl mb-4">Contact Us</h3>
          <div className="space-y-2">
            <div className="flex items-start gap-2">
              <FaPhoneAlt />
              <span className="font-semibold">+91 9876543210</span>
            </div>
            <div className="flex items-center gap-2">
  <FaEnvelope className="text-black text-[18px] shrink-0" />
  <a
    href="mailto:wedtype@weddingcards.com"
    className="font-semibold hover:underline break-all"
  >
    wedtype@weddingcards.com
  </a>
</div>
            <p className="font-semibold">Operating hours: 10.00Am to 10.00Pm</p>
            <p className="font-semibold">Monday - Sunday</p>
          </div>
        </div>
      </div>

      {/* Bottom Copyright */}
      <div className="border-t border-gray-400 mt-8 pt-4 text-center text-xs sm:text-sm md:text-base">
        <p className="flex items-center justify-center gap-2 font-semibold">
          <FaRegCopyright />
          Wed Knot Craft India Private Limited. All Rights Reserved.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
