import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const Login = () => {
  const [activeTab, setActiveTab] = useState('login');
  const navigate = useNavigate();

  // Login form state
  const [loginEmail, setLoginEmail] = useState('');
  const [loginPassword, setLoginPassword] = useState('');
  const [loginErrors, setLoginErrors] = useState({});

  // Sign up form state
  const [signupName, setSignupName] = useState('');
  const [signupEmail, setSignupEmail] = useState('');
  const [signupPassword, setSignupPassword] = useState('');
  const [signupErrors, setSignupErrors] = useState({});

  const validateEmail = (email) => {
    return /^[\w-.]+@([\w-]+\.)+[\w-]{2,4}$/.test(email);
  };

  const handleLoginSubmit = (e) => {
    e.preventDefault();
    const errors = {};

    if (!loginEmail) errors.email = 'Email is required';
    else if (!validateEmail(loginEmail)) errors.email = 'Invalid email format';

    if (!loginPassword) errors.password = 'Password is required';

    setLoginErrors(errors);

    if (Object.keys(errors).length === 0) {
      // Navigate to home
      navigate('/');
    }
  };

  const handleSignupSubmit = (e) => {
    e.preventDefault();
    const errors = {};

    if (!signupName) errors.name = 'Name is required';
    if (!signupEmail) errors.email = 'Email is required';
    else if (!validateEmail(signupEmail)) errors.email = 'Invalid email format';

    if (!signupPassword) errors.password = 'Password is required';

    setSignupErrors(errors);

    if (Object.keys(errors).length === 0) {
      alert('Account created successfully!');
      setActiveTab('login');
    }
  };

  return (
    <div className="min-h-screen bg-[#e8e6f5] flex justify-center items-center px-4">
      <div className="bg-white w-full max-w-5xl rounded-md shadow-md p-6 flex flex-col md:flex-row">
        {/* Tabs */}
        <div className="w-full md:w-1/2 p-4">
          <div className="flex justify-center space-x-8 mb-8">
            <button
              className={`text-2xl font-bold ${activeTab === 'login' ? 'border-b-4 border-black' : 'text-gray-500'}`}
              onClick={() => setActiveTab('login')}
            >
              Login
            </button>
            <button
              className={`text-2xl font-bold ${activeTab === 'signup' ? 'border-b-4 border-black' : 'text-gray-500'}`}
              onClick={() => setActiveTab('signup')}
            >
              Sign Up
            </button>
          </div>

          {/* Login Form */}
          {activeTab === 'login' && (
            <form onSubmit={handleLoginSubmit}>
              <h2 className="text-xl font-semibold mb-6">Login to my Account</h2>

              <div className="mb-4">
                <label className="block mb-1 font-medium">Email</label>
                <input
                  type="email"
                  value={loginEmail}
                  onChange={(e) => setLoginEmail(e.target.value)}
                  placeholder="Enter Email"
                  className="w-full px-4 py-2 border rounded outline-none"
                />
                {loginErrors.email && <p className="text-red-600 text-sm mt-1">{loginErrors.email}</p>}
              </div>

              <div className="mb-4">
                <label className="block mb-1 font-medium">Password</label>
                <input
                  type="password"
                  value={loginPassword}
                  onChange={(e) => setLoginPassword(e.target.value)}
                  placeholder="Enter Password"
                  className="w-full px-4 py-2 border rounded outline-none"
                />
                {loginErrors.password && <p className="text-red-600 text-sm mt-1">{loginErrors.password}</p>}
              </div>

              <button
                type="submit"
                className="bg-[#c0392b] hover:bg-[#a93226] w-full text-white py-2 rounded font-semibold"
              >
                Login & Continue
              </button>
              <p className="mt-4 text-center text-[#c0392b] font-semibold cursor-pointer">Forgot Password</p>
            </form>
          )}

          {/* Sign Up Form */}
          {activeTab === 'signup' && (
            <form onSubmit={handleSignupSubmit}>
              <h2 className="text-xl font-semibold mb-6">Create a New Account</h2>

              <div className="mb-4">
                <label className="block mb-1 font-medium">Full Name</label>
                <input
                  type="text"
                  value={signupName}
                  onChange={(e) => setSignupName(e.target.value)}
                  placeholder="Enter Name"
                  className="w-full px-4 py-2 border rounded outline-none"
                />
                {signupErrors.name && <p className="text-red-600 text-sm mt-1">{signupErrors.name}</p>}
              </div>

              <div className="mb-4">
                <label className="block mb-1 font-medium">Email</label>
                <input
                  type="email"
                  value={signupEmail}
                  onChange={(e) => setSignupEmail(e.target.value)}
                  placeholder="Enter Email"
                  className="w-full px-4 py-2 border rounded outline-none"
                />
                {signupErrors.email && <p className="text-red-600 text-sm mt-1">{signupErrors.email}</p>}
              </div>

              <div className="mb-4">
                <label className="block mb-1 font-medium">Password</label>
                <input
                  type="password"
                  value={signupPassword}
                  onChange={(e) => setSignupPassword(e.target.value)}
                  placeholder="Enter Password"
                  className="w-full px-4 py-2 border rounded outline-none"
                />
                {signupErrors.password && <p className="text-red-600 text-sm mt-1">{signupErrors.password}</p>}
              </div>

              <button
                type="submit"
                className="bg-[#27ae60] hover:bg-[#219150] w-full text-white py-2 rounded font-semibold"
              >
                Sign Up
              </button>
            </form>
          )}
        </div>

        {/* Right Side Image or Content (optional) */}
        
      </div>
    </div>
  );
};

export default Login;
