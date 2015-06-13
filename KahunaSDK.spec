Pod::Spec.new do |s|
  s.name = 'KahunaSDK'
  s.version = '2.0.0'
  s.summary = 'Mobile A/B testing, personalization & analytics in one powerful platform.'
  s.description = 'Kahuna! Mobile A/B testing, personalization & analytics in one powerful platform.'
  s.homepage = 'https://www.Kahuna.com'
  s.license = { :type => 'Commercial', :text => 'See https://www.Kahuna.com/tos' }
  s.author = { 'Kahuna' => 'support@Kahuna.com' }
  s.social_media_url = 'https://twitter.com/Kahuna'
  s.platform = :ios, '6.0'
  s.requires_arc = true
  s.source = { :git => 'https://github.com/sharekris/Kahuna-iOS-SDK.git' }
  s.frameworks = 'CoreLocation', 'SystemConfiguration', 'UIKit'
  s.xcconfig = { 'OTHER_LDFLAGS' => '-ObjC' }
  s.preserve_paths = 'Kahuna.framework'
  s.documentation_url = 'https://www.Kahuna.com/contact'
  s.public_header_files = 'Kahuna.framework/Headers/*.h'
  s.vendored_frameworks = 'Kahuna.framework'
end
