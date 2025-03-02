<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader @show-login="showLoginModal = true" />
    
    <div class="container mx-auto px-4 py-6">
      <div class="max-w-3xl mx-auto">
        <!-- Hero section -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-100 p-6 mb-6">
          <div class="text-center">
            <h1 class="text-3xl font-bold mb-4 text-gray-900">
              <span class="text-primary-600">Globetrotter</span> Challenge
            </h1>
            
            <p class="text-lg text-gray-600 mb-6 max-w-2xl mx-auto">
              Test your knowledge of famous places around the world in this
              fun travel guessing game!
            </p>
            
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
              <button 
                @click="startGame" 
                class="bg-primary-600 hover:bg-primary-700 text-white px-6 py-3 rounded-md font-medium transition-colors"
              >
                Start Playing
              </button>
              
              <button 
                v-if="userStore.isLoggedIn"
                @click="showChallengeModal = true" 
                class="bg-gray-100 hover:bg-gray-200 text-gray-800 px-6 py-3 rounded-md font-medium transition-colors"
              >
                Challenge a Friend
              </button>
            </div>
          </div>
        </div>
        
        <!-- How to play section -->
        <div class="bg-white rounded-lg shadow-sm border border-gray-100 p-6">
          <h2 class="text-xl font-medium mb-4 text-gray-900">How to Play</h2>
          
          <div class="space-y-4">
            <div class="flex items-start">
              <div class="flex-shrink-0 text-2xl mr-3">🧩</div>
              <div>
                <h3 class="font-medium text-gray-900">Solve the Clues</h3>
                <p class="text-gray-600">Read the clues about a famous destination and guess which place it refers to.</p>
              </div>
            </div>
            
            <div class="flex items-start">
              <div class="flex-shrink-0 text-2xl mr-3">🎯</div>
              <div>
                <h3 class="font-medium text-gray-900">Select the Right Answer</h3>
                <p class="text-gray-600">Choose from multiple destinations to test your travel knowledge.</p>
              </div>
            </div>
            
            <div class="flex items-start">
              <div class="flex-shrink-0 text-2xl mr-3">📖</div>
              <div>
                <h3 class="font-medium text-gray-900">Learn Fun Facts</h3>
                <p class="text-gray-600">Discover interesting trivia about each destination after you've made your guess.</p>
              </div>
            </div>
            
            <div class="flex items-start">
              <div class="flex-shrink-0 text-2xl mr-3">🏆</div>
              <div>
                <h3 class="font-medium text-gray-900">Challenge Friends</h3>
                <p class="text-gray-600">Invite your friends to see who knows more about world destinations!</p>
              </div>
            </div>
          </div>
          
          <div class="mt-6 text-center" v-if="!userStore.isLoggedIn">
            <button 
              @click="showLoginModal = true"
              class="text-primary-600 hover:text-primary-700 bg-primary-50 hover:bg-primary-100 px-4 py-2 rounded-md text-sm font-medium transition-colors"
            >
              Create a Profile
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- User registration modal -->
    <div v-if="showLoginModal" class="fixed inset-0 flex items-center justify-center z-50">
      <div class="absolute inset-0 bg-black bg-opacity-25" @click="showLoginModal = false"></div>
      <div class="z-10 max-w-md w-full mx-4">
        <UserRegistration @success="handleLoginSuccess" />
      </div>
    </div>
    
    <!-- Challenge modal -->
    <div v-if="showChallengeModal" class="fixed inset-0 flex items-center justify-center z-50">
      <div class="absolute inset-0 bg-black bg-opacity-25" @click="showChallengeModal = false"></div>
      <div class="z-10 max-w-md w-full mx-4">
        <ChallengeInvite @close="showChallengeModal = false" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useUserStore } from '@/stores/user';
import AppHeader from '@/components/AppHeader.vue';
import UserRegistration from '@/components/UserRegistration.vue';
import ChallengeInvite from '@/components/ChallengeInvite.vue';

const router = useRouter();
const userStore = useUserStore();

const showLoginModal = ref(false);
const showChallengeModal = ref(false);

const startGame = () => {
  router.push('/game');
};

const handleLoginSuccess = () => {
  showLoginModal.value = false;
};
</script>