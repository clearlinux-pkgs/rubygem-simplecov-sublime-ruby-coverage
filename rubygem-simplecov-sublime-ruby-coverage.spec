#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-simplecov-sublime-ruby-coverage
Version  : 1.0.0
Release  : 3
URL      : https://rubygems.org/downloads/simplecov-sublime-ruby-coverage-1.0.0.gem
Source0  : https://rubygems.org/downloads/simplecov-sublime-ruby-coverage-1.0.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-docile
BuildRequires : rubygem-echoe
BuildRequires : rubygem-metaclass
BuildRequires : rubygem-mocha
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-simplecov
BuildRequires : rubygem-simplecov-html
BuildRequires : rubygem-test-unit

%description
SimpleCov Sublime Ruby Coverage Formatter gem
=============================================

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n simplecov-sublime-ruby-coverage-1.0.0
gem spec %{SOURCE0} -l --ruby > rubygem-simplecov-sublime-ruby-coverage.gemspec

%build
gem build rubygem-simplecov-sublime-ruby-coverage.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
simplecov-sublime-ruby-coverage-1.0.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/simplecov-sublime-ruby-coverage-1.0.0
ruby -v -I.:lib:test test*/*_test.rb || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/simplecov-sublime-ruby-coverage-1.0.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/Manifest
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/lib/simplecov-sublime-ruby-coverage.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/simplecov-sublime-ruby-coverage.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/fixtures/app/controllers/sample_controller.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/fixtures/app/models/user.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/fixtures/sample.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/fixtures/test-fixtures-app-controllers-sample_controller_rb.csv
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/fixtures/test-fixtures-app-models-user_rb.csv
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/fixtures/test-fixtures-sample_rb.csv
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/simplecov-sublime-ruby-coverage-1.0.0/test/simplecov-sublime-ruby-coverage_test.rb
/usr/lib64/ruby/gems/2.3.0/specifications/simplecov-sublime-ruby-coverage-1.0.0.gemspec
